#include <cstdlib>
#include <ctime>
#include <iostream>

struct Route {
    int x = 0;
    int y = 0;
    // for Python to know the len of this array
    int size = 0;
};

extern "C" Route* getRoute() {
    srand(time(nullptr));
    int count = rand() % 100;
    if (count == 0)
        count = 1;

    auto routes = new Route[count];
    for (int i = 0; i < count; i++) {
        routes[i].x = rand() % 10000;
        routes[i].y = rand() % 10000;
    }
    routes[0].size = count;
    return routes;
}

extern "C" void freeRoutes(Route* routes) {
    if (routes != nullptr) {
        delete[] routes;
        std::cout << "Freed all routes\n";
    }
}
