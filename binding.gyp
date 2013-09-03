{
	'targets': [
		{
			'target_name': 'dbus',
			'sources': [
				'src/dbus.cc'
			],
			'conditions': [
				['OS=="linux"', {
					'defines': [
						'LIB_EXPAT=expat'
					],
					'cflags': [
						'<!@(pkg-config --cflags dbus-1)',
						'<!@(pkg-config --cflags expat)'
					],
					'ldflags': [
						'<!@(pkg-config  --libs-only-L --libs-only-other dbus-1)',
						'<!@(pkg-config  --libs-only-L --libs-only-other expat)'
					],
					'libraries': [
						'<!@(pkg-config  --libs-only-l --libs-only-other dbus-1)',
						'<!@(pkg-config  --libs-only-l --libs-only-other expat)'
					]
				}]
			]
		}
	]
}
