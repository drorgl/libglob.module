{
	'variables':{
		'library' : 'static_library',
	},
	
	'targets':
	[
		{
			'target_name': 'libglob',
			'type':'static_library',
			
			
			'defines':[],
			'conditions':[
				['OS != "linux"',{
					'include_dirs':[
						'.',
					],
					'direct_dependent_settings': {
						'include_dirs': [
							'.',
						],
					 },
					'sources':[
						'glob.c',
						'glob.h'
					],
				}],
			]
		},
		
		
	]
}