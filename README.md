![logo](logo.png)
-
:wind_chime: Extracts information from CHANGELOG.md files. :octocat:

[![Build Status](https://travis-ci.org/MyRealityCoding/chime.svg?branch=deploy)](https://travis-ci.org/MyRealityCoding/chime)
![Docker-Stars](https://img.shields.io/docker/stars/bitbrain/chime.svg)
![Docker-Pulls](https://img.shields.io/docker/pulls/bitbrain/chime.svg)

**:package: [Getting started](#getting-started) |**
**:rocket: [License](#license) |**
**:pencil: [Changelog](CHANGELOG.md)**

---

# Getting started

To run *chime* type:
```bash
docker run -v (pwd):/chime bitbrain/chime:latest <CHANGELOG.md file> <command>
```

# Commands

* `version` retrieves the latest version
* `text <version>` retrieves the text of the given version. Otherwise retrieves the latest text.

# License

This software is licensed under the [Apache 2 License](LICENSE).
