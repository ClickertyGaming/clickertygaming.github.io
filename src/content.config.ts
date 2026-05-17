import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "astro/zod";
const blog = defineCollection({
    loader: glob({ pattern: "**/*.{md,mdx}", base: "./src/content/blog" }),
    schema: z.object({
        title: z.string(),
        description: z.string().default(""),
        author: z.string(),
        tags: z.string().default(""),
        important: z.boolean().default(false),
    }),
    
});
const music = defineCollection({
    loader: glob({ pattern: "**/*.{md,mdx}", base: "./src/content/music" }),
    schema: z.object({
        title: z.string(),
        creator: z.string(),
        year: z.number(),
        genre: z.string(),
        length: z.string(),
        type: z.string(),
        cover: z.string().default(""),
        id: z.number(),
        url: z.string()
    })
});
export const collections = { blog, music };