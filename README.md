# captcha-svg
Python script to bypass an SVG-based CAPTCHA (2025 edition).

This script integrates with the 2Captcha API: [https://2captcha.com/api-docs](https://2captcha.com/api-docs)

Before sending the image to the solver, we preprocess it by forcing a **white background**—this makes the characters clearer and significantly improves success rates. Basic OCR can work as well, depending on the complexity of the CAPTCHA.

For another example (using Puppeteer & reCAPTCHA), check out:  
👉 [https://github.com/FORTBRIDGE-UK/Captcha](https://github.com/FORTBRIDGE-UK/Captcha)

