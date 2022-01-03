import glob
import os


def get_tags_dir(post_dir_):
    filenames = glob.glob(post_dir_ + '*html')
    total_tags = []
    for filename in filenames:
        f = open(filename, 'r', encoding='utf8')
        crawl = False
        for line in f:
            if crawl:
                current_tags = line.strip().split(':')
                if current_tags[0] == 'tags':
                    if (current_tags[1].strip().startswith('[')):
                        clean_tag = ''.join(c for c in current_tags[1] if c not in '[]')
                        list_tags = map(str.strip, clean_tag.split(','))
                        total_tags.extend(list_tags)
                    else:
                        list_tags = map(str.strip, current_tags[1].strip().split())
                        total_tags.extend(list_tags)
                    crawl = False
                    break
            if line.strip() == '---':
                if not crawl:
                    crawl = True
                else:
                    crawl = False
                    break
        f.close()
    total_tags = set(total_tags)
    return total_tags


def write_tag_pages(tag_dir_, total_tags_):
    old_tags = glob.glob(tag_dir_ + '*.md')
    for tag in old_tags:
        os.remove(tag)
    if not os.path.exists(tag_dir_):
        os.makedirs(tag_dir_)

    for tag in total_tags_:
        tag_filename = tag_dir_ + tag.replace(' ', '_') + '.md'
        f = open(tag_filename, 'a')
        write_str = '---\nlayout: tagpage\ntitle: \"Tag: ' + tag + '\"\ntag: ' + tag + '\nrobots: noindex\n---\n'
        f.write(write_str)
        f.close()

    return None


def main():
    post_dir = '_posts/'
    tag_dir = 'tag/'

    total_tags = get_tags_dir(post_dir_=post_dir)
    for tag in total_tags:
        print(tag)
    write_tag_pages(tag_dir, total_tags)
    print("Tags generated, count", len(total_tags))

main()