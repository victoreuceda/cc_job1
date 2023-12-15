# Compiler settings
CXX = g++
CXXFLAGS = -Wall -std=c++17

# Target executable name
TARGET = executable.out

# Source files
SOURCES = fibonacci.cpp

# Rule for making the target
$(TARGET): $(SOURCES)
	$(CXX) $(CXXFLAGS) $(SOURCES) -o $(TARGET)

# Clean rule
clean:
	rm -f $(TARGET)

# Rule for executing the program
run: $(TARGET)
	./$(TARGET)
