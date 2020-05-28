# Generated by Django 3.0.6 on 2020-05-28 08:19

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20200527_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'image', 'code', 'blockquote'])), ('code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('sql', 'SQL'), ('yaml', 'YAML')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.core.blocks.TextBlock(identifier='code', label='Code'))], label='Code')), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('caption', wagtail.core.blocks.CharBlock(label='Caption', required=False)), ('float', wagtail.core.blocks.ChoiceBlock(choices=[('right', 'Right'), ('left', 'Left'), ('center', 'Center')], label='Float', required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], label='Size', required=False))])), ('video', wagtail.core.blocks.StructBlock([('video', wagtail.embeds.blocks.EmbedBlock(label='Video')), ('caption', wagtail.core.blocks.CharBlock(label='Caption', required=False)), ('float', wagtail.core.blocks.ChoiceBlock(choices=[('right', 'Right'), ('left', 'Left'), ('center', 'Center')], label='Float', required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], label='Size', required=False))]))]),
        ),
    ]