#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>
#include <algorithm>

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
    Body b;
    b.x = 4.84143144246472090e+00;
    b.vx = 1.66007664274403694e-03 * DAYS_PER_YEAR;
    b.y = -1.16032004402742839e+00;
    b.vy = 7.69901118419740425e-03 * DAYS_PER_YEAR;
    b.z = -1.03622044471123109e-01;
    b.vz = -6.90460016972063023e-05 * DAYS_PER_YEAR;
    b.mass = 9.54791938424326609e-04 * SOLAR_MASS;
    return b;
}

Body saturn() {
    Body b;
    b.x = 8.34336671824457987e+00;
    b.vx = -2.76742510726862411e-03 * DAYS_PER_YEAR;
    b.y = 4.12479856412430479e+00;
    b.vy = 4.99852801234917238e-03 * DAYS_PER_YEAR;
    b.z = -4.03523417114321381e-01;
    b.vz = 2.30417297573763929e-05 * DAYS_PER_YEAR;
    b.mass = 2.85885980666130812e-04 * SOLAR_MASS;
    return b;
}

Body uranus() {
    Body b;
    b.x = 1.28943695621391310e+01;
    b.vx = 2.96460137564761618e-03 * DAYS_PER_YEAR;
    b.y = -1.51111514016986312e+01;
    b.vy = 2.37847173959480950e-03 * DAYS_PER_YEAR;
    b.z = -2.23307578892655734e-01;
    b.vz = -2.96589568540237556e-05 * DAYS_PER_YEAR;
    b.mass = 4.36624404335156298e-05 * SOLAR_MASS;
    return b;
}

Body neptune() {
    Body b;
    b.x = 1.53796971148509165e+01;
    b.vx = 2.68067772490389322e-03 * DAYS_PER_YEAR;
    b.y = -2.59193146099879641e+01;
    b.vy = 1.62824170038242295e-03 * DAYS_PER_YEAR;
    b.z = 1.79258772950371181e-01;
    b.vz = -9.51592254519715870e-05 * DAYS_PER_YEAR;
    b.mass = 5.15138902046611451e-05 * SOLAR_MASS;
    return b;
}

Body sun() {
    Body b;
    b.x = 0;
    b.vx = 0;
    b.y = 0;
    b.vy = 0;
    b.z = 0;
    b.vz = 0;
    b.mass = SOLAR_MASS;
    return b;
}

class NBodySystem {
private:
    std::vector<Body> bodies;

public:
    NBodySystem()
        : bodies(5)
    {
        bodies[0] = sun();
        bodies[1] = jupiter();
        bodies[2] = saturn();
        bodies[3] = uranus();
        bodies[4] = neptune();

        double px = 0.0;
        double py = 0.0;
        double pz = 0.0;
        for (int i = 0; i < bodies.size(); ++i) {
            px += bodies[i].vx * bodies[i].mass;
            py += bodies[i].vy * bodies[i].mass;
            pz += bodies[i].vz * bodies[i].mass;
        }
        bodies[0].offsetMomentum(px, py, pz);
    }

    void advance(const double dt) {
        const int N = (bodies.size() - 1) * bodies.size() / 2;
        std::vector<double> dx(N), dy(N), dz(N), distance(N), dmag(N), mag(N);

        int k = 0;
        for (int i = 0; i < bodies.size() - 1; ++i) {
            for (int j = i + 1; j < bodies.size(); ++j, ++k) {
                dx[k] = bodies[i].x - bodies[j].x;
                dy[k] = bodies[i].y - bodies[j].y;
                dz[k] = bodies[i].z - bodies[j].z;
            }
        }

        for (int i = 0; i < N; i += 2) {
            distance[i] = std::sqrt(dx[i] * dx[i] + dy[i] * dy[i] + dz[i] * dz[i]);
            distance[i + 1] = std::sqrt(dx[i + 1] * dx[i + 1] + dy[i + 1] * dy[i + 1] + dz[i + 1] * dz[i + 1]);

            dmag[i] = dt / (distance[i] * distance[i] * distance[i]);
            dmag[i + 1] = dt / (distance[i + 1] * distance[i + 1] * distance[i + 1]);
        }

        k = 0;
        for (int i = 0; i < bodies.size() - 1; ++i) {
            for (int j = i + 1; j < bodies.size(); ++j, ++k) {
                double jmm = bodies[j].mass * dmag[k];
                bodies[i].vx -= dx[k] * jmm;
                bodies[i].vy -= dy[k] * jmm;
                bodies[i].vz -= dz[k] * jmm;

                double imm = bodies[i].mass * dmag[k];
                bodies[j].vx += dx[k] * imm;
                bodies[j].vy += dy[k] * imm;
                bodies[j].vz += dz[k] * imm;
            }
        }

        for (int i = 0; i < bodies.size(); ++i) {
            bodies[i].x += dt * bodies[i].vx;
            bodies[i].y += dt * bodies[i].vy;
            bodies[i].z += dt * bodies[i].vz;
        }
    }

    double energy() {
        double e = 0.0;

        for (int i = 0; i < bodies.size(); ++i) {
            Body iBody = bodies[i];
            e += 0.5 * iBody.mass *
                (iBody.vx * iBody.vx +
                 iBody.vy * iBody.vy +
                 iBody.vz * iBody.vz);

            for (int j = i + 1; j < bodies.size(); ++j) {
                Body jBody = bodies[j];

                double dx = iBody.x - jBody.x;
                double dy = iBody.y - jBody.y;
                double dz = iBody.z - jBody.z;

                double distance = std::sqrt(dx * dx + dy * dy + dz * dz);
                e -= (iBody.mass * jBody.mass) / distance;
            }
        }

        return e;
    }
};

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(false);
    int n = 0;
    while (*argv[1]) {
        n = n * 10 + (*argv[1]++ - '0');
    }

    NBodySystem bodies;
    std::cout << std::setprecision(9) << bodies.energy() << '\n';
    for (int i = 0; i < n; ++i)
        bodies.advance(0.01);
    std::cout << bodies.energy();
    return 0;
}
