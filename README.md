simple-gae-boilerplate
======================

A more robust Google App Engine boilerplate with localization support based on the simplified, frontend focused, [Simple-GAE-Boilerplate](https://github.com/burkeshartsis/simple-gae-boilerplate)

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
- Url Mapping for supported languages
	- supported languages are detected automatically after added to the l10n folder
- Session saving for languague preference persistance

What it still doesn't have:

- SASS/SCSS/LESS
- Database setup