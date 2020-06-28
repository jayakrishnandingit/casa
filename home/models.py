from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet


# Create your models here.
class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FileCategory(Timestamp):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def __str__(self):
        return '%s' % self.name


class FileUpload(Timestamp):
    name = models.CharField(max_length=200, null=False, blank=False)
    category = models.OneToOneField(FileCategory, related_name='files', on_delete=models.CASCADE)
    uploaded_file = models.FileField(upload_to='files/')

    def __str__(self):
        return '%s - %s' % (self.name, self.category)


@register_snippet
class SkillCategory(models.Model):
    name = models.CharField(max_length=500, unique=True)

    panels = [
        FieldPanel('name')
    ]

    def __str__(self):
        return self.name


@register_snippet
class Skills(models.Model):
    category = models.ForeignKey(
        SkillCategory,
        on_delete=models.CASCADE,
        related_name='skills'
    )
    name = models.CharField(max_length=500)

    panels = [
        SnippetChooserPanel('category'),
        FieldPanel('name')
    ]

    def __str__(self):
        return '%s - %s' % (self.name, self.category)


class SocialMediaBtnBlock(blocks.StructBlock):
    text = blocks.CharBlock()
    link = blocks.URLBlock()
    icon = blocks.CharBlock()
    btn_class = blocks.CharBlock()

    class Meta:
        template = 'home/partials/blocks/_social_media.html'


class HomePage(Page):
    hero = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('bgimage', ImageChooserBlock(required=False))
    ])

    social_media_cta = StreamField([
        ('cta', SocialMediaBtnBlock())
    ])

    about_me = StreamField([
        ('heading', blocks.CharBlock(classname="full title", default='')),
        ('paragraph', blocks.RichTextBlock(default=''))
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('hero'),
        StreamFieldPanel('social_media_cta'),
        StreamFieldPanel('about_me')
    ]
