def get_by_id(collection, id):
    posts = list(filter(lambda item: item['id'] == id , collection['posts']))
    try: 
        return posts[0]
    except IndexError:
        return 'No posts found'