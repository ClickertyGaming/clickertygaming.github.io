import { getCollection } from "astro:content";
import rss from '@astrojs/rss';
import { SITE_TITLE, SITE_DESC } from "../consts";

export async function GET(context) {
    const posts = await getCollection('blog');
    return rss({
        title: SITE_TITLE,
        description: SITE_DESC,
        trailingSlash: false,
        site: context.site,
        items: posts.map((post) => ({
            title: post.data.title,
            author: post.data.author,
            tags: post.data.tags,
            important: post.data.important,
            link: '/blog/'+post.id,
        }))
    });
}