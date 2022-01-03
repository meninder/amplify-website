import glob


def get_post_meta(post_dir_):
    filenames = glob.glob(post_dir_ + '*html')
    filenames.sort()
    dct = {}
    for i, filename in enumerate(filenames):
        dct[i] = {}
        f = open(filename, 'r', encoding='utf8')
        next(f)
        for line in f:
            current_meta_line = line.strip().split(':')
            if current_meta_line[0] == '---':
                break
            elif current_meta_line[0] == 'title':
                dct[i]['title'] = current_meta_line[1]
            elif current_meta_line[0] == 'date':
                dct[i]['date'] = current_meta_line[1].split()[0]
            elif current_meta_line[0] == 'caption':
                dct[i]['caption'] = current_meta_line[1]
            elif current_meta_line[0] == 'tags':
                dct[i]['tags'] = (', ').join(current_meta_line[1].strip().split())

        f.close()

    return dct


def write_dct(dct_):
    with open("list_of_posts.txt", "w") as f:
        for i,post in dct_.items():
            f.write('*' * 20)
            f.write('\n')
            for meta_tag, meta_value in post.items():
                f.write(f"{meta_tag}:{meta_value}\n")


dct = get_post_meta(post_dir_='_posts/')
write_dct(dct_=dct)



