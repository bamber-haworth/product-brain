name: Generate Slide Deck
description: This skill generates a slide deck presentation based on a given topic and content. The presentation uses the company branding guidelines and includes a title slide, heading slides, body slides, and a thank you slide.

> Before starting, read `product-context/BRAND.md` for colours, fonts, and asset locations. Read `product-context/PRODUCTS.md` for correct product and company names.

## Use Company Branding

Any slide decks created should be stored in the outputs folder of this repository, and should follow the branding guidelines as outlined in `product-context/BRAND.md`.

Check if Montserrat and Roboto fonts are installed. If not, install them via Homebrew, and use them in the presentation as specified in `product-context/BRAND.md`. The header font is Montserrat bold and the body is Roboto. If these fonts are not available, try to install them. If installation is not possible, use the closest available alternatives.

The visual style of the slides should match the master slide deck template (see `product-context/assets/brand/` for screenshots and reference files), which uses the same branding guidelines. Match the styling as closely as possible to ensure consistency. Extract any images or graphics from the master slide deck that are relevant to the content of the presentation, and use them in the appropriate slides.

The accent colours are defined in `product-context/BRAND.md`.

Every page with a white background should use the wave asset as a footer, taking up the bottom 10% of the page (it is fine to crop or stretch the asset as needed to fit the width of the page). The asset is at `product-context/assets/brand/wave.png`.

The logo should be used in the center of the title slide and the thank you slide. Use the logo at `product-context/assets/brand/logo.png`. The logo should be 120px wide and maintain its aspect ratio. The logo should be centred on the slide, and should line up perfectly with the center of the text on the title slide and the thank you slide.

The title slide should have spacing of 20px between items such as the logo, the title, and the subtitle. They should be vertically centred on the slide.

Heading slides, which introduce new sections of the presentation, should use the accent colours as background, with white text in Montserrat bold. The title should be centered on these slides. There should be a white logo in the bottom right corner of these slides (`product-context/assets/brand/logo_white.png`). The heading slides should not use the wave footer asset. The heading text should have an underline graphic extracted from the master slide deck, placed directly below the heading text with a gap of 10px. The underline graphic should be centered with the heading text. Examples of heading slides can be found in the screenshots in `product-context/assets/brand/` — match the images in these as closely as possible.

The body slides should have a white background with black text in Roboto standard.

All titles, subtitles, and quotes should be centre aligned on the page and should have a width of 838px. Slide headings and body content should use 95% of the full width of the slide.

Slide headings should be left aligned and should have no line under them.

Body text should be left aligned and should have a maximum width of 1200px. The body text should be placed below the heading, with a gap of 20px between the heading and the body text. Each line should have a bullet point styled with a small filled square (▪) in the brand teal colour (see `product-context/BRAND.md`), with body text in black. The bullet markers should be indented by 15px and the text should be in Roboto. The spacing between each line of body text should be 1.5x the font size.

Never place a vertical dividing line down the middle of a slide (e.g. between two columns). Two-column layouts should use whitespace alone to separate the columns.

Slides should use widescreen layout. Content should be centered on the screen, with no cut offs or misalignments.

When referencing products or the company by name, always use the full name on first reference (see `product-context/PRODUCTS.md` for correct names), then you may use the short name on subsequent references. Never use abbreviations or alternative names.

Use bullet points when appropriate to improve readability, but avoid using more than five bullet points per slide to maintain clarity and focus.

When including images or graphics, ensure they are high quality and relevant to the content being presented. Use captions to provide context for the images when necessary.

After generating, look at images of each of the slides to see where the alignment is incorrect, and adjust them accordingly.
