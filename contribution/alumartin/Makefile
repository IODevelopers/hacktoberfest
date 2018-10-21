CXX=g++
CXXFLAGS=-std=c++11 -lncurses -g

snake: snake.o
	$(CXX) snake.o -o $@ $(CXXFLAGS)

snake.o: snake.cpp common.hpp
	$(CXX) -c snake.cpp $(CXXFLAGS)

clean:
	rm *.o snake
