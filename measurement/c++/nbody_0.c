/* The Computer Language Benchmarks Game
   https://salsa.debian.org/benchmarksgame-team/benchmarksgame/

   contributed by Mark C. Lewis
   modified slightly by Chad Whipkey
   converted from java to c++,added sse support, by Branimir Maksimovic
   modified by Vaclav Zeman
   modified by Vaclav Haisman to use explicit SSE2 intrinsics and constexpr
   modified by Lukasz C

   NOTE: There are some modifications to make compatible to old versions (C++98)

   Result:
    - 5000 -> -0.169075164 
-0.16902
    - 500000 -> -0.169075164
-0.169096567
    
    -0.169075164
    0.0545777498


    -0.169075163828524
1.61811467117757

-0.169075163828524
-0.101841358910445
*/
#include <iostream>
#include <iomanip>
#include <cmath>

#define PI 3.141592653589793
#define SOLAR_MASS (4 * PI * PI)
#define DAYS_PER_YEAR 365.24

class Body {
public:
    double x, vx, y, vy, z, vz;
    double mass;

    Body& offsetMomentum(const double px, const double py, const double pz) {
        vx = -px / SOLAR_MASS;
        vy = -py / SOLAR_MASS;
        vz = -pz / SOLAR_MASS;
        return *this;
    }
};

Body jupiter() {
    Body j;
    j.x = 4.84143144246472090e+00;
    j.vx = 1.66007664274403694e-03 * DAYS_PER_YEAR;
    j.y = -1.16032004402742839e+00;
    j.vy = 7.69901118419740425e-03 * DAYS_PER_YEAR;
    j.z = -1.03622044471123109e-01;
    j.vz = -6.90460016972063023e-05 * DAYS_PER_YEAR;
    j.mass = 9.54791938424326609e-04 * SOLAR_MASS;
    return j;
}

Body saturn() {
    Body s;
    s.x = 8.34336671824457987e+00;
    s.vx = -2.76742510726862411e-03 * DAYS_PER_YEAR;
    s.y = 4.12479856412430479e+00;
    s.vy = 4.99852801234917238e-03 * DAYS_PER_YEAR;
    s.z = -4.03523417114321381e-01;
    s.vz = 2.30417297573763929e-05 * DAYS_PER_YEAR;
    s.mass = 2.85885980666130812e-04 * SOLAR_MASS;
    return s;
}

Body uranus() {
    Body u;
    u.x = 1.28943695621391310e+01;
    u.vx = 2.96460137564761618e-03 * DAYS_PER_YEAR;
    u.y = -1.51111514016986312e+01;
    u.vy = 2.37847173959480950e-03 * DAYS_PER_YEAR;
    u.z = -2.23307578892655734e-01;
    u.vz = -2.96589568540237556e-05 * DAYS_PER_YEAR;
    u.mass = 4.36624404335156298e-05 * SOLAR_MASS;
    return u;
}

Body neptune() {
    Body n;
    n.x = 1.53796971148509165e+01;
    n.vx = 2.68067772490389322e-03 * DAYS_PER_YEAR;
    n.y = -2.59193146099879641e+01;
    n.vy = 1.62824170038242295e-03 * DAYS_PER_YEAR;
    n.z = 1.79258772950371181e-01;
    n.vz = -9.51592254519715870e-05 * DAYS_PER_YEAR;
    n.mass = 5.15138902046611451e-05 * SOLAR_MASS;
    return n;
}

Body sun() {
    Body s;
    s.x = 0;
    s.vx = 0;
    s.y = 0;
    s.vy = 0;
    s.z = 0;
    s.vz = 0;
    s.mass = SOLAR_MASS;
    return s;
}

class NBodySystem {
private:
    Body bodies[5];
    static const unsigned int bodies_size = 5;

public:
    NBodySystem() {
        bodies[0] = sun();
        bodies[1] = jupiter();
        bodies[2] = saturn();
        bodies[3] = uranus();
        bodies[4] = neptune();

        double px = 0.0;
        double py = 0.0;
        double pz = 0.0;
        for (unsigned i = 0; i != bodies_size; ++i) {
            px += bodies[i].vx * bodies[i].mass;
            py += bodies[i].vy * bodies[i].mass;
            pz += bodies[i].vz * bodies[i].mass;
        }
        bodies[0].offsetMomentum(px, py, pz);
    }

    void advance(const double dt) {
        const unsigned N = ((bodies_size - 1) * bodies_size) >> 1;
        struct R {
            double dx, dy, dz;
        };
        static R r[1000];
        static double mag[1000];

        for (unsigned int i = 0, k = 0; i != bodies_size - 1; ++i) {
            for (unsigned int j = i + 1; j != bodies_size; ++j, ++k) {
                r[k].dx = bodies[i].x - bodies[j].x;
                r[k].dy = bodies[i].y - bodies[j].y;
                r[k].dz = bodies[i].z - bodies[j].z;
            }
        }

        for (unsigned int i = 0; i != N; ++i) {
            mag[i] = dt / (r[i].dx * r[i].dx + r[i].dy * r[i].dy + r[i].dz * r[i].dz);
        }

        for (unsigned int i = 0, k = 0; i != bodies_size - 1; ++i) {
            Body &iBody = bodies[i];
            for (unsigned int j = i + 1; j != bodies_size; ++j, ++k) {
                Body &jBody = bodies[j];
                double jmm = jBody.mass * mag[k];
                iBody.vx -= r[k].dx * jmm;
                iBody.vy -= r[k].dy * jmm;
                iBody.vz -= r[k].dz * jmm;

                double imm = iBody.mass * mag[k];
                jBody.vx += r[k].dx * imm;
                jBody.vy += r[k].dy * imm;
                jBody.vz += r[k].dz * imm;
            }
        }

        for (unsigned int i = 0; i != bodies_size; ++i) {
            Body &iBody = bodies[i];
            iBody.x += dt * iBody.vx;
            iBody.y += dt * iBody.vy;
            iBody.z += dt * iBody.vz;
        }
    }

    double energy() {
        double e = 0.0;

        for (unsigned int i = 0; i != bodies_size; ++i) {
            Body const &iBody = bodies[i];
            e += 0.5 * iBody.mass * (iBody.vx * iBody.vx + iBody.vy * iBody.vy + iBody.vz * iBody.vz);

            for (unsigned int j = i + 1; j != bodies_size; ++j) {
                Body const &jBody = bodies[j];

                double dx = iBody.x - jBody.x;
                double dy = iBody.y - jBody.y;
                double dz = iBody.z - jBody.z;

                double distance = sqrt(dx * dx + dy * dy + dz * dz);
                e -= (iBody.mass * jBody.mass) / distance;
            }
        }
        return e;
    }
};

int main(int argc, char **argv) {
    std::ios_base::sync_with_stdio(false);
    int n = 0;
    while (*argv[1]) {
        n = n * 10 + (*argv[1]++ - '0');
    }

    NBodySystem bodies;
    std::cout << std::setprecision(15) << bodies.energy() << '\n';
    for (int i = 0; i < n; ++i)
        bodies.advance(0.01);
    std::cout << std::setprecision(15) << bodies.energy() << '\n';
}
