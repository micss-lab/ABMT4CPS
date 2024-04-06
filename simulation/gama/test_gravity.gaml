model test_gravity

global parent: physical_world {
	bool use_native <- false;
	bool accurate_collision_detection <- false;
	float restitution <- 0.0;
	float friction <- 0.0;
	
	float step <- 0.0001;
	geometry shape <- box(100, 100, 0);
	
	init {
		do register([self]);
		
		create ball with:[location:{50,50,100}];
	}
	
	reflex save_result when: every(100#cycle) {
		save ball[0].location.z to: "gravity_gama.txt" rewrite: (cycle = 0) ? true : false;
	}
	
	reflex end_simulation when: cycle = 99999 {
		do pause;
    }
}

species ball skills: [dynamic_body] {
	geometry shape <- sphere(10);

	float mass <- 1.0;
	float damping <- 0.0;
	float restitution <- 0.0;
	float friction <- 0.0;
	
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
