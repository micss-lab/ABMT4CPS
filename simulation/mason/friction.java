package sim.app.collisions;

import sim.engine.*;
import sim.field.continuous.*;
import ec.util.*;
import sim.physics2D.util.*;
import java.awt.*;
import sim.util.Double2D;

import sim.physics2D.*;
import sim.physics2D.integrator.*;

public class Collisions extends SimState
{
    public double xMin = 0;
    public double xMax = 200;
    public double yMin = 0;
    public double yMax = 200;

    public Continuous2D fieldEnvironment;

    public Collisions(long seed)
    {
        this(seed, 200, 200);
    }

    public Collisions(long seed, int width, int height)
    {
        super(seed);
        xMax = width;
        yMax = height;
        createGrids();
    }

    void createGrids()
    {
        fieldEnvironment = new Continuous2D(25, (xMax - xMin), (yMax - yMin));
    }

    int numCircles = 1;
    public int getNumCircles() { return numCircles; }
    public void setNumCircles(int val) { if (val >= 0) numCircles = val; }

    int numRectangles = 5;
    public int getNumRectangles() { return numRectangles; }
    public void setNumRectangles(int val) { if (val >= 0) numRectangles = val; }

    int size = 10;
    public int getSize() { return size; }
    public void setSize(int val) { if (val >= 0) size = val; }

    int wallPos = 0;
    public int getWallPos() { return wallPos; }
    public void setWallPos(int val) { wallPos = val; };

    // Resets and starts a simulation
    public void start()
    {
        super.start();  // clear out the schedule
        createGrids();

        PhysicsEngine2D objPE = new PhysicsEngine2D();
        objPE.setODESolver(new ODEEulerSolver());

        Double2D pos;
        Double2D vel;

        Wall wall;
        // WALLS
        // HORIZ

        /*
          pos = new Double2D(100,wallPos);
          wall = new Wall(pos, 250, 8);
          fieldEnvironment.setObjectLocation(wall, new sim.util.Double2D(pos.x, pos.y));
          objPE.register(wall);
        */

        pos = new Double2D(100,wallPos);
        wall = new Wall(pos, 200 - wallPos * 2, 6);
        fieldEnvironment.setObjectLocation(wall, new sim.util.Double2D(pos.x, pos.y));
        objPE.register(wall);

        pos = new Double2D(100,200 - wallPos);
        wall = new Wall(pos, 200 - wallPos * 2, 6);
        fieldEnvironment.setObjectLocation(wall, new sim.util.Double2D(pos.x, pos.y));
        objPE.register(wall);

        // VERT
        pos = new Double2D(wallPos,100);
        wall = new Wall(pos, 6, 200 - wallPos * 2);
        fieldEnvironment.setObjectLocation(wall, new sim.util.Double2D(pos.x, pos.y));
        objPE.register(wall);

        pos = new Double2D(200 - wallPos,100);
        wall = new Wall(pos, 6, 200 - wallPos * 2);
        fieldEnvironment.setObjectLocation(wall, new sim.util.Double2D(pos.x, pos.y));
        objPE.register(wall);

        MobileCircle circ;
        pos = new Double2D(15, 185);
        circ = new MobileCircle(pos, new Double2D(10.0,0.0), size, "1");
        fieldEnvironment.setObjectLocation(circ, new sim.util.Double2D(pos.x, pos.y));
        objPE.register(circ);
        schedule.scheduleRepeating(circ);

        // schedule the physics engine
        schedule.scheduleRepeating(objPE);
    }

    public static void main(String[] args)
    {
        doLoop(Collisions.class, args);
        System.exit(0);
    }
}
