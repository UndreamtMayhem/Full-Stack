from datetime import datetime
from blogsetup import Blog


# TODO add custom form validation
class BlogLogic(object):
    def __init__(self, body, caption, description, name, image_url, is_public, title):
        self.body = body
        self.caption = caption
        self.date_uploaded = datetime.now()
        self.description = description
        self.likes = 0
        self.name = name
        self.image_url = image_url
        self.is_public = is_public
        self.title = title
    def __repr__(self):
        return(
            self.body +
            self.caption +
            str(self.date_uploaded) +
            self.description +
            str(self.likes) +
            self.name +
            self.image_url +
            str(self.is_public) +
            self.title)
    def create_blog(self, blog_user):
        """Create blog."""
        first_blog = Blog(
            body=self.body,
            caption=self.caption,
            date_uploaded=datetime.now(),
            description=self.description,
            is_public=True,
            image_url=self.image_url,
            likes=self.likes,
            name=self.name,
            title=self.title,
            user=blog_user,
        )
        return first_blog