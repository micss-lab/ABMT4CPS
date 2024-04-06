model test_collision

global parent: physical_world {
	bool use_native <- false;
	bool accurate_collision_detection <- false;
	float restitution <- 1.0;
	float friction <- 0.0;
	
	float step <- 0.0001;
	geometry shape <- box(100, 100, 0);
	
	init {
		do register([self]);
		
		create ground with:[location:{0,0,0}];
		create ball with:[location:{1,0,100}];
	}
	
	reflex save_result when: every(100#cycle) {
		save ball[0].location.x + ball[0].location.y + ball[0].location.z to: "collision_gama.txt" rewrite: (cycle = 0) ? true : false;
	}
	
	reflex end_simulation when: cycle = 99999 {
		do pause;
    }
}

species ground skills: [static_body] {
	geometry shape <- cone3D(100, 100);

	aspect default {
		draw shape color:#blue wireframe:true;
	}
}

species ball skills: [dynamic_body] {
	geometry shape <- sphere(5);

	float mass <- 1.0;
	float damping <- 0.0;
	float restitution <- 1.0;
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
			species ground;
		    species ball;		
		}
	}
}
