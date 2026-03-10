# Django Blog System

A simple and clean **Blog System built with Django**.
This project demonstrates how to build a blog with **categories, tags, comments, and post management**.

## Features

* Create and manage blog posts
* Category system for organizing posts
* Tag system for flexible filtering
* Post status management (Draft / Published)
* Comment system with approval
* Post view counter
* Estimated reading time calculation
* Slug based SEO-friendly URLs
* Featured (Pinned) posts
* Image upload for posts

---

## Models Overview

### Category

Used to group posts by topic.

Fields:

* `name` – Category name
* `slug` – URL friendly identifier
* `description` – Category description

Methods:

* `get_absolute_url()` – Returns category page URL
* `post_count()` – Counts published posts in category

---

### Tag

Tags allow flexible labeling of posts.

Fields:

* `name` – Tag name
* `slug` – URL friendly identifier

Methods:

* `get_absolute_url()` – Returns tag page URL
* `post_count()` – Counts published posts with this tag

---

### Post

Main blog article model.

Fields:

* `title` – Post title
* `slug` – SEO friendly URL
* `content` – Full article content
* `excerpt` – Short preview text
* `category` – Related category
* `tags` – Many-to-many relationship with tags
* `image` – Post cover image
* `status` – Draft or Published
* `is_pinned` – Featured post flag
* `view_count` – Number of views
* `created_at` – Creation timestamp
* `updated_at` – Last update timestamp

Methods:

* `get_absolute_url()` – Post detail page
* `reading_time()` – Estimated reading time
* `approved_comments()` – Returns approved comments
* `comment_count()` – Number of approved comments

---

### Comment

Handles user comments for posts.

Fields:

* `post` – Related post
* `name` – Comment author
* `email` – Author email
* `body` – Comment text
* `is_approved` – Comment moderation status
* `created_at` – Comment creation time

---

## Relationships

* **Category → Post** (One-to-Many)
* **Post → Tag** (Many-to-Many)
* **Post → Comment** (One-to-Many)

---

## Example Features Implemented

* Automatic slug generation using `slugify`
* Comment moderation system
* Post filtering by category or tag
* Reading time calculation (200 words per minute)

---

## Technologies Used

* Python
* Django
* SQLite (default)
* Django ORM

---

## Installation

```bash
git clone https://github.com/yourusername/django-blog.git
cd django-blog
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Run server

```bash
python manage.py runserver
```

---

## Future Improvements

* User authentication
* Like system
* Search functionality
* Pagination
* REST API

---

## License

This project is open-source and available for educational purposes.
