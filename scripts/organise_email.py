#!/usr/bin/env python3
"""
Email organiser - follows skills/email-organiser/SKILL.md
Uses Gmail IMAP via Python imaplib

Credentials are read from environment variables:
  GMAIL_ADDR     - your Gmail address
  GMAIL_PASSWORD - your Gmail App Password
"""
import imaplib
import os
import re
import datetime
from email.header import decode_header

# --- Config ---
IMAP_HOST = 'imap.gmail.com'
EMAIL_ADDR = os.environ.get('GMAIL_ADDR', 'bamber@audiostack.ai')
PASSWORD = os.environ.get('GMAIL_PASSWORD', '')

COLLEAGUE_DOMAINS = ['audiostack.ai', 'siroc.com', 'siroc-group.com']

CUSTOMER_DOMAINS = [
    'azerion.com', 'bigfm.de', 'topradio.be', 'powerkraut.nl', 'pocketfm.com',
    'lotofhappiness.nl', 'prisaradio.com', 'talpanetwork.com', 'news.co.uk',
    'atsw-media.de', 'octaveip.com', 'global.com', 'techways.online',
    'higuita.amsterdam', 'lotteryasaservice.nl', 'adpaq.com', 'tritondigital.com',
    'draftdigital.nl', 'oelsnitz.de', 'germanwahnsinn.de', 'grupoprisa.com',
]

# Domains of cold-email / sales engagement tools — auto-deleted
SALES_DOMAINS = [
    'outreach.io', 'salesloft.com', 'reply.io', 'lemlist.com',
    'apollo.io', 'mailshake.com', 'woodpecker.co', 'yesware.com',
    'mixmax.com', 'groove.co', 'persistiq.com', 'klenty.com',
]

# Subject phrases that are highly indicative of cold sales outreach
SALES_SUBJECT_QUERIES = [
    '(SUBJECT "wanted to reach out")',
    '(SUBJECT "partnership opportunity")',
    '(SUBJECT "collaboration opportunity")',
    '(SUBJECT "free demo")',
    '(SUBJECT "schedule a demo")',
    '(SUBJECT "book a demo")',
    '(SUBJECT "I help companies like")',
]

# Known recruiter agency domains — auto-deleted
RECRUITER_DOMAINS = [
    'getrecruitedpro.co.uk', 'michaelpage.com', 'michaelpage.co.uk',
    'hays.com', 'hays.co.uk', 'reed.co.uk', 'robertwalters.com',
    'robertwalters.co.uk', 'totaljobs.com', 'cwjobs.co.uk',
    'technojobs.co.uk', 'linkedin.com',
]

# Subject phrases strongly associated with recruiter outreach
RECRUITER_SUBJECT_QUERIES = [
    '(SUBJECT "candidates")',
    '(SUBJECT "job opportunity")',
    '(SUBJECT "open role")',
    '(SUBJECT "new role")',
    '(SUBJECT "exciting role")',
    '(SUBJECT "recruitment")',
    '(SUBJECT "your next hire")',
    '(SUBJECT "talent acquisition")',
    '(SUBJECT "we are hiring")',
    '(SUBJECT "join our team")',
]

CATEGORY_LABELS = [
    '2FA and Login Emails',
    'Colleagues',
    'Customers',
    'Task Alerts',
    'Calendar Alerts',
    'Newsletters and Subscriptions',
    'Support Inbox',
    'Invoices / Transactions',
    'Other Emails',
]

# Descriptive tags applied on top of category labels so emails are easier to understand at a glance.
# Each tag maps to a list of IMAP subject queries.
CONTENT_TAGS = {
    'Action Required': [
        '(SUBJECT "action required")',
        '(SUBJECT "response needed")',
        '(SUBJECT "please respond")',
        '(SUBJECT "approval needed")',
        '(SUBJECT "your approval")',
        '(SUBJECT "RSVP")',
        '(SUBJECT "deadline")',
    ],
    'Invoice / Receipt': [
        '(SUBJECT "invoice")',
        '(SUBJECT "receipt")',
        '(SUBJECT "payment confirmation")',
        '(SUBJECT "billing statement")',
        '(SUBJECT "your order")',
    ],
    'Contract / Agreement': [
        '(SUBJECT "contract")',
        '(SUBJECT "agreement")',
        '(SUBJECT "NDA")',
        '(SUBJECT "please sign")',
        '(SUBJECT "signature required")',
        '(SUBJECT "DocuSign")',
    ],
    'Feature Request': [
        '(SUBJECT "feature request")',
        '(SUBJECT "feature suggestion")',
        '(SUBJECT "product feedback")',
        '(SUBJECT "enhancement request")',
    ],
    'Bug / Issue': [
        '(SUBJECT "bug report")',
        '(SUBJECT "not working")',
        '(SUBJECT "broken")',
        '(SUBJECT "error report")',
    ],
    'Introduction': [
        '(SUBJECT "introduction")',
        '(SUBJECT "intro:")',
        '(SUBJECT "connecting you")',
        '(SUBJECT "meet ")',
    ],
}

PRIORITY_DOMAINS = set(COLLEAGUE_DOMAINS + CUSTOMER_DOMAINS)

# --- Connect ---
print("Connecting to Gmail IMAP...")
mail = imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT := 993)
mail.login(EMAIL_ADDR, PASSWORD)
print("Connected.\n")

# --- Helper: extract email address from From header ---
def get_from_addr(from_hdr):
    match = re.search(r'[\w.\-+]+@[\w.\-]+', from_hdr or '')
    return match.group(0).lower() if match else ''

# --- Helper: get domain from address ---
def get_domain(addr):
    return addr.split('@')[1] if '@' in addr else ''

# --- Helper: fetch From domain for a UID ---
def fetch_from_domain(uid):
    s, d = mail.uid('fetch', uid, '(BODY[HEADER.FIELDS (FROM)])')
    if s == 'OK' and d[0]:
        raw = d[0][1].decode(errors='replace')
        return get_domain(get_from_addr(raw))
    return ''

# --- Helper: filter UIDs to those NOT from priority domains ---
def non_priority_uids(uids):
    return [u for u in uids if fetch_from_domain(u) not in PRIORITY_DOMAINS]

# --- Helper: apply label (and optionally remove from inbox) ---
def label_messages(uids, label, keep_in_inbox=False):
    if not uids:
        return 0
    uid_str = b','.join(uids)
    mail.uid('COPY', uid_str, f'"{label}"')
    if not keep_in_inbox:
        mail.uid('STORE', uid_str, '+FLAGS', '\\Deleted')
    return len(uids)

# --- Helper: build nested IMAP OR query for a list of FROM domains ---
def or_from_domains(domains):
    terms = [f'FROM "@{d}"' for d in domains]
    while len(terms) > 1:
        paired = []
        for i in range(0, len(terms), 2):
            if i + 1 < len(terms):
                paired.append(f'(OR {terms[i]} {terms[i+1]})')
            else:
                paired.append(terms[i])
        terms = paired
    return terms[0]

# --- Ensure labels exist ---
print("=== Creating labels if needed ===")
status, raw_folders = mail.list()
existing = set()
for f in raw_folders:
    parts = f.decode(errors='replace').split('"')
    name = parts[-2] if len(parts) >= 3 else f.decode().split()[-1]
    existing.add(name.strip())

for label in CATEGORY_LABELS + list(CONTENT_TAGS.keys()):
    if label not in existing:
        res, _ = mail.create(f'"{label}"')
        print(f"  Created: {label}" if res == 'OK' else f"  FAILED to create: {label}")
    else:
        print(f"  Exists:  {label}")

# --- Step 1: 2FA / login emails ---
print("\n=== Step 1: 2FA and Login Emails ===")
queries = [
    '(FROM "@accounts.google.com")',
    '(FROM "@account.microsoft.com")',
    '(FROM "@github.com" SUBJECT "login")',
    '(SUBJECT "verification code")',
    '(SUBJECT "login alert")',
    '(SUBJECT "account activity")',
    '(SUBJECT "two-factor")',
    '(SUBJECT "sign-in attempt")',
]
labelled = 0
for q in queries:
    mail.select('INBOX')
    status, data = mail.uid('search', None, q)
    if status == 'OK' and data[0]:
        labelled += label_messages(data[0].split(), '2FA and Login Emails')
mail.expunge()
print(f"  Labelled: {labelled}")

# --- Step 2: Calendar alerts (before Colleagues so invite notifications from colleagues are caught here) ---
print("\n=== Step 2: Calendar Alerts ===")
cal_queries = [
    '(SUBJECT "Accepted:")',
    '(SUBJECT "Declined:")',
    '(SUBJECT "Tentative:")',
    '(SUBJECT "Canceled:")',
    '(SUBJECT "Updated invitation")',
    '(SUBJECT "New event")',
    '(SUBJECT "invitation")',
    '(SUBJECT "meeting reminder")',
    '(SUBJECT "event update")',
    '(SUBJECT "calendar invite")',
]
labelled = 0
for q in cal_queries:
    mail.select('INBOX')
    status, data = mail.uid('search', None, q)
    if status == 'OK' and data[0]:
        labelled += label_messages(data[0].split(), 'Calendar Alerts')
mail.expunge()
print(f"  Labelled: {labelled}")

# --- Step 3: Colleagues (keep in inbox) ---
print("\n=== Step 3: Colleagues ===")
mail.select('INBOX')
status, data = mail.uid('search', None, or_from_domains(COLLEAGUE_DOMAINS))
labelled = 0
if status == 'OK' and data[0]:
    labelled = label_messages(data[0].split(), 'Colleagues', keep_in_inbox=True)
print(f"  Labelled: {labelled}")

# --- Step 4: Customers (keep in inbox) ---
print("\n=== Step 4: Customers ===")
mail.select('INBOX')
status, data = mail.uid('search', None, or_from_domains(CUSTOMER_DOMAINS))
labelled = 0
if status == 'OK' and data[0]:
    labelled = label_messages(data[0].split(), 'Customers', keep_in_inbox=True)
print(f"  Labelled: {labelled}")

# --- Step 5: Task alerts ---
print("\n=== Step 5: Task Alerts ===")
task_domains = [
    'asana.com', 'app.asana.com', 'mail.asana.com', 'jira.com', 'trello.com',
    'monday.com', 'linear.app', 'notifications.atlassian.net',
]
mail.select('INBOX')
status, data = mail.uid('search', None, or_from_domains(task_domains))
labelled = 0
if status == 'OK' and data[0]:
    labelled = label_messages(data[0].split(), 'Task Alerts')
mail.expunge()
print(f"  Labelled: {labelled}")

# --- Step 6: Newsletters and Subscriptions ---
print("\n=== Step 6: Newsletters and Subscriptions ===")
newsletter_queries = [
    '(FROM "@mailchimp.com")',
    '(FROM "@substack.com")',
    '(FROM "@beehiiv.com")',
    '(FROM "@sendgrid.net" SUBJECT "newsletter")',
    '(SUBJECT "unsubscribe")',
    '(SUBJECT "newsletter")',
]
labelled = 0
for q in newsletter_queries:
    mail.select('INBOX')
    status, data = mail.uid('search', None, q)
    if status == 'OK' and data[0]:
        labelled += label_messages(data[0].split(), 'Newsletters and Subscriptions')
mail.expunge()
print(f"  Labelled: {labelled}")

# --- Step 7: Support Inbox (support@audiostack.ai, Intercom, Harvestr) ---
print("\n=== Step 7: Support Inbox ===")
support_queries = [
    '(TO "support@audiostack.ai")',
    '(FROM "@intercom.io")',
    '(FROM "@intercom.com")',
    '(FROM "@harvestr.io")',
    '(FROM "@harvestrapp.com")',
]
labelled = 0
for q in support_queries:
    mail.select('INBOX')
    status, data = mail.uid('search', None, q)
    if status == 'OK' and data[0]:
        labelled += label_messages(data[0].split(), 'Support Inbox')
mail.expunge()
print(f"  Labelled: {labelled}")

# --- Step 8: Sales Emails (auto-delete, no label) ---
print("\n=== Step 8: Sales Emails (auto-delete) ===")
deleted = 0

# Domain-based: known sales engagement tools
mail.select('INBOX')
status, data = mail.uid('search', None, or_from_domains(SALES_DOMAINS))
if status == 'OK' and data[0]:
    uids = non_priority_uids(data[0].split())
    if uids:
        uid_str = b','.join(uids)
        mail.uid('COPY', uid_str, '[Gmail]/Trash')
        mail.uid('STORE', uid_str, '+FLAGS', '\\Deleted')
        deleted += len(uids)

# Subject-based: unmistakable cold-email phrases
for q in SALES_SUBJECT_QUERIES:
    mail.select('INBOX')
    status, data = mail.uid('search', None, q)
    if status == 'OK' and data[0]:
        uids = non_priority_uids(data[0].split())
        if uids:
            uid_str = b','.join(uids)
            mail.uid('COPY', uid_str, '[Gmail]/Trash')
            mail.uid('STORE', uid_str, '+FLAGS', '\\Deleted')
            deleted += len(uids)

mail.expunge()
print(f"  Deleted: {deleted}")

# --- Step 9: Recruiter Emails (auto-delete, no label) ---
print("\n=== Step 9: Recruiter Emails (auto-delete) ===")
deleted = 0

mail.select('INBOX')
status, data = mail.uid('search', None, or_from_domains(RECRUITER_DOMAINS))
if status == 'OK' and data[0]:
    uids = non_priority_uids(data[0].split())
    if uids:
        uid_str = b','.join(uids)
        mail.uid('COPY', uid_str, '[Gmail]/Trash')
        mail.uid('STORE', uid_str, '+FLAGS', '\\Deleted')
        deleted += len(uids)

for q in RECRUITER_SUBJECT_QUERIES:
    mail.select('INBOX')
    status, data = mail.uid('search', None, q)
    if status == 'OK' and data[0]:
        uids = non_priority_uids(data[0].split())
        if uids:
            uid_str = b','.join(uids)
            mail.uid('COPY', uid_str, '[Gmail]/Trash')
            mail.uid('STORE', uid_str, '+FLAGS', '\\Deleted')
            deleted += len(uids)

mail.expunge()
print(f"  Deleted: {deleted}")

# --- Step 10: Other Emails (catch-all for anything remaining) ---
print("\n=== Step 9: Other Emails (catch-all) ===")
mail.select('INBOX')
status, data = mail.uid('search', None, 'ALL')
labelled = 0
if status == 'OK' and data[0]:
    other_uids = non_priority_uids(data[0].split())
    labelled = label_messages(other_uids, 'Other Emails')
mail.expunge()
print(f"  Labelled: {labelled}")

# --- Step 11: Trash all emails >30 days old (exclude priority senders) ---
print("\n=== Step 11: Trash emails >30 days old ===")
mail.select('INBOX')
cutoff_30 = (datetime.date.today() - datetime.timedelta(days=30)).strftime('%d-%b-%Y')
status, data = mail.uid('search', None, f'(BEFORE {cutoff_30})')
trashed = 0
if status == 'OK' and data[0]:
    safe = non_priority_uids(data[0].split())
    if safe:
        uid_str = b','.join(safe)
        mail.uid('COPY', uid_str, '[Gmail]/Trash')
        mail.uid('STORE', uid_str, '+FLAGS', '\\Deleted')
        mail.expunge()
        trashed = len(safe)
print(f"  Trashed: {trashed}")

# --- Step 12: Archive emails >7 days old (exclude priority senders) ---
print("\n=== Step 12: Archive emails >7 days old ===")
mail.select('INBOX')
cutoff_7 = (datetime.date.today() - datetime.timedelta(days=7)).strftime('%d-%b-%Y')
status, data = mail.uid('search', None, f'(BEFORE {cutoff_7})')
archived = 0
if status == 'OK' and data[0]:
    safe = non_priority_uids(data[0].split())
    if safe:
        uid_str = b','.join(safe)
        mail.uid('STORE', uid_str, '+FLAGS', '\\Deleted')
        mail.expunge()
        archived = len(safe)
print(f"  Archived: {archived}")

# --- Tagging pass: apply descriptive tags across all mail ---
# Tags are additional labels stacked on top of category labels.
# Searching All Mail means already-processed emails are tagged too.
print("\n=== Tagging Pass ===")
mail.select('"[Gmail]/All Mail"')
for tag, queries in CONTENT_TAGS.items():
    tagged = 0
    for q in queries:
        status, data = mail.uid('search', None, q)
        if status == 'OK' and data[0]:
            uid_str = b','.join(data[0].split())
            mail.uid('COPY', uid_str, f'"{tag}"')
            tagged += len(data[0].split())
    if tagged:
        print(f"  {tag}: {tagged}")

mail.logout()
print("\n=== Done! ===")
