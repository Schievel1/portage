# Copyright 2015-2016 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2

doc = """fetches plug-in module for repoman.
Performs fetch related checks on ebuilds."""
__doc__ = doc[:]


module_spec = {
	'name': 'fetches',
	'description': doc,
	'provides':{
		'fetches-module': {
			'name': "fetches",
			'sourcefile': "fetches",
			'class': "FetchChecks",
			'description': doc,
			'functions': ['check'],
			'func_desc': {
			},
			'mod_kwargs': ['portdb', 'qatracker', 'repo_settings', 'vcs_settings',
			],
			'func_kwargs': {'xpkg': None, 'checkdir': None,
				'checkdir_relative': None, 'changed': None,
				'src_uri_error': 'Future',
			},
		},
	}
}
