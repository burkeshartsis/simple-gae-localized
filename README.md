simple-gae-localized
======================

A more robust Google App Engine boilerplate with localization support based on the simplified, frontend focused, [Simple-GAE-Boilerplate](https://github.com/burkeshartsis/simple-gae-boilerplate).

======================

The goal here is to allow for quick rollout of traditionally structured websites that need robust localization support. It's agile, simple, and powerful.

What it shares with [Simple-GAE-Boilerplate](https://github.com/burkeshartsis/simple-gae-boilerplate)

- Preconfigured App.yaml, handlers, and routes
- Set up for base handlers (universal/site wide handlers)
- Jinja2 templating
- HTML5 Boilerplate
	- js
		- jQuery 1.9.1 minimized
		- Modernizr 2.6.2 minimized
		- Respond1.1.0 minimized
	- css
		- Normalize
		- Normalize minimized
	- HTML
		- IE html tag classes
- Best practice App Engine folder structure

What's new!

- Localization support for text strings via [ARB](https://code.google.com/p/arb/wiki/ApplicationResourceBundleSpecification)
	- this json like format is robust and works great with [Google's Translator Toolkit](https://support.google.com/translate/toolkit/topic/22235?hl=en&ref_topic=22228)
- Automatic url Mapping for supported languages
- Session saving for languague preference persistance
- Global and localized data variables for clean and easy seperation of translated content

What it still doesn't have:

- SASS/SCSS/LESS
- Database setup

Acknowledgements
----------------
Special thanks goes out to [Patrick Guiness](https://github.com/patrickguiness) for his help debugging. Not sure how many hours I would have waisted without him.