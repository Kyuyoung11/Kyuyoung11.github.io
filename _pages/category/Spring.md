---
title: "Spring"
layout: category-page
permalink: category/spring/
author_profile: true
sidebar_main: true
---


{% assign posts = site.categories.spring %}
{% for post in posts %} {% include category-page.html type=page.entries_layout %} {% endfor %}
