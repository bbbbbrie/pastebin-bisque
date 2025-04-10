// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'pb',
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/bbbbbrie/pastebin-bisque' },{ icon: 'gitlab', label: 'GitLab', href: 'https://gitlab.com/brie/pastebin-bisque' }],
			sidebar: [
				{
					label: 'pastebin-bisque',
					items: [
						// Each item here is one entry in the navigation menu.
						{ label: 'Overview', slug: 'overview' },
						{ label: 'Installing', slug: 'install' },
						{ label: 'Usage', slug: 'usage' },
						{ label: 'Explore', slug: 'explore' },
						{ label: 'Contributing', slug: 'contributing' },
					],
				}//,
//				{
//					label: 'Reference',
//					autogenerate: { directory: 'reference' },
//				},
			],
		}),
	],
});
