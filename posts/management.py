from .models import Post, Comment

def save_default(sender, **kwargs):
    data = [
        # {
        #     'post': 'hello',
        #     'comments': ['hello2', 'world']
        # }
    ]

    for sample in data:
        post = Post.objects.get_or_create(content=sample['post'])[0]
        for comment in sample['comments']:
            Comment.objects.get_or_create(post_id=post, content=comment)

    print('Default data saved')
