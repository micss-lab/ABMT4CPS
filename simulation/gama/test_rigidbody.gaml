model test_collision

global parent: physical_world {
	bool use_native <- true;
	bool accurate_collision_detection <- true;
	float step <- 0.0001;
	geometry shape <- box(100, 100, 0);
	
	init {
		do register([self]);
				
		create ball with:[location:{50,50,0}];
		create ball with:[location:{51,50,11}];
		create ball with:[location:{52,50,22}];
		create ball with:[location:{53,50,33}];
		create ball with:[location:{54,50,44}];
	}
}

species ball skills: [dynamic_body] {
	geometry shape <- cube(10);
	
	aspect default {
		draw shape color:#red wireframe:true;
	}
}

experiment Display type: gui {
	output {	
		display Display type:3d background:rgb(0,0,0) camera:#isometric {
			graphics world {
				draw shape color:#white wireframe:true;
			}
		    species ball;		
		}
	}
}
