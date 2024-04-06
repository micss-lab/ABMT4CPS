package SimplePhysics;

import java.awt.Color;

import repast.simphony.context.Context;
import repast.simphony.context.space.physics.PhysicsSpaceFactoryFinder;
import repast.simphony.dataLoader.ContextBuilder;
import repast.simphony.engine.environment.RunEnvironment;
import repast.simphony.parameter.Parameters;
import repast.simphony.space.continuous.SimpleCartesianAdder;
import repast.simphony.space.physics.PhysicsSpace;
import repast.simphony.space.physics.RigidBodyFactory;

import com.bulletphysics.dynamics.RigidBody;

/**
 * @author Eric Tatara
 */
public class SimplePhysicsContextCreator implements ContextBuilder {

	public Context build(Context context) {

		double[] size = {1000, 1000, 1000};
		
		Parameters p = RunEnvironment.getInstance().getParameters();
		float targetParticleSize = ((Double)p.getValue("targetParticleSize")).floatValue();
		float targetParticleMass = ((Double)p.getValue("targetParticleMass")).floatValue();
		float projectileRadius = ((Double)p.getValue("projectileRadius")).floatValue();
		float projectileMass = ((Double)p.getValue("projectileMass")).floatValue();
		float projectileVelocity = ((Double)p.getValue("projectileVelocity")).floatValue();
		boolean gravityOn = (Boolean)p.getValue("gravityOn");
		boolean platformOn = (Boolean)p.getValue("platformOn");
		
		// create the physics space
		PhysicsSpace space = PhysicsSpaceFactoryFinder.createPhysicsSpaceFactory(null)
		.createPhysicsSpace("Physics Space", context, new SimpleCartesianAdder(),
						new repast.simphony.space.continuous.WrapAroundBorders(), size);
		space.setStepSize((float) 0.01);
		
		if (!gravityOn)
		  space.setGravity(0, 0, 0);
		
		// 3D style size / phsyics body size = Display cell size (0.01)
		float scale = targetParticleSize * 0.01f;
		
		// build the target blocks
		int platformOffset = 400;
//		for (float x=1; x<=10; x+=targetParticleSize){
//			for (float y=1; y<=10; y+=targetParticleSize){
//				for (float z=1; z<=10; z+=targetParticleSize){
//					PhysicsAgent agent = new PhysicsAgent();
//					agent.setColor(pickColor(x));
//					context.add(agent);
//					agent.setScale(new float[]{scale,scale,scale});
//					
//					float[] loc = new float[]{platformOffset+x, platformOffset+y, 
//							platformOffset+z};
//					
//					RigidBody body = RigidBodyFactory.createCubeBody(targetParticleSize, 
//							targetParticleMass, loc);	
//					space.addObject(agent, body);
//				}
//			}
//		}
				
		// create a projectile
		scale = 2* projectileRadius * 0.01f;
		Projectile projectile1 = new Projectile("1");
		projectile1.setColor(Color.CYAN);
		context.add(projectile1);
		projectile1.setScale(new float[]{scale,scale,scale});
		float offset = platformOffset - targetParticleSize / 2;
		float[] loc = new float[]{400,offset+10,400};
		RigidBody body = RigidBodyFactory.createSphereBody(projectileRadius, projectileMass, loc);		
		space.addObject(projectile1, body);
		space.setLinearVelocity(projectile1, 0,0,0);
		
		// create a projectile
		scale = 2* projectileRadius * 0.01f;
		Projectile projectile2 = new Projectile("2");
		projectile2.setColor(Color.CYAN);
		context.add(projectile2);
		projectile2.setScale(new float[]{scale,scale,scale});
		offset = platformOffset - targetParticleSize / 2;
		loc = new float[]{400,offset+20,400};
		body = RigidBodyFactory.createSphereBody(projectileRadius, projectileMass, loc);		
		space.addObject(projectile2, body);
		space.setLinearVelocity(projectile2, 0,0,0);
		
		// create a projectile
		scale = 2* projectileRadius * 0.01f;
		Projectile projectile3 = new Projectile("3");
		projectile3.setColor(Color.CYAN);
		context.add(projectile3);
		projectile3.setScale(new float[]{scale,scale,scale});
		offset = platformOffset - targetParticleSize / 2;
		loc = new float[]{400,offset+30,400};
		body = RigidBodyFactory.createSphereBody(projectileRadius, projectileMass, loc);		
		space.addObject(projectile3, body);
		space.setLinearVelocity(projectile3, 0,0,0);
		
		// optionally create a target platform
		if (platformOn){
			PhysicsAgent platform = new PhysicsAgent();
			platform.setColor(new Color(0,100,0));
			context.add(platform);
			offset = platformOffset - targetParticleSize / 2;
			loc = new float[]{400,offset,400};
			platform.setScale(new float[]{2,0.01f, 2});
			body = RigidBodyFactory.createBoxBody(200, 2, 200, 0, loc);	
			space.addObject(platform, body);
		}
		
		return context;
	}

	private Color pickColor(float x){
		if (x<=2)
			return Color.RED;
		else if (x>2 && x<=4)
			return Color.ORANGE;
		else if (x>4 && x<=6)
			return Color.YELLOW;
		else if (x>6 && x<=8)
			return Color.GREEN;
		else return Color.BLUE;
	}
}
