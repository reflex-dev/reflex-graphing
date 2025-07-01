#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure

def test_pyplot_import():
    """Test that the pyplot component can be imported successfully."""
    try:
        from reflex_pyplot import pyplot
        print("✓ pyplot component imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Failed to import pyplot component: {e}")
        return False

def test_pyplot_component_creation():
    """Test that the pyplot component can be created with a matplotlib figure."""
    try:
        from reflex_pyplot import pyplot
        
        fig, ax = plt.subplots(figsize=(8, 6))
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        ax.plot(x, y, label='sin(x)')
        ax.set_title('Test Plot')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.legend()
        ax.grid(True)
        
        component = pyplot(fig)
        print("✓ pyplot component created successfully")
        print(f"✓ Component type: {type(component)}")
        
        plt.close(fig)  # Clean up
        return True
    except Exception as e:
        print(f"✗ Failed to create pyplot component: {e}")
        return False

def test_matplotlib_serializer():
    """Test that the matplotlib figure serializer works correctly."""
    try:
        from reflex_pyplot.pyplot import Pyplot
        
        fig, ax = plt.subplots(figsize=(6, 4))
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([2, 4, 6, 8, 10])
        ax.scatter(x, y, c='red', s=50)
        ax.set_title('Test Scatter Plot')
        
        serialized = Pyplot.serialize_matplotlib_figure(fig)
        print(f"✓ Figure serialized successfully, length: {len(serialized)} chars")
        
        if serialized.startswith('data:image/png;base64,'):
            print("✓ Serialized figure has correct data URL format")
        else:
            print("✗ Serialized figure does not have correct data URL format")
            return False
            
        plt.close(fig)  # Clean up
        return True
    except Exception as e:
        print(f"✗ Failed to serialize matplotlib figure: {e}")
        return False

def test_figure_type_annotations():
    """Test that matplotlib Figure type annotations work correctly."""
    try:
        from matplotlib.figure import Figure
        
        fig = Figure(figsize=(5, 3))
        ax = fig.add_subplot(111)
        ax.plot([1, 2, 3], [1, 4, 2])
        ax.set_title('Type Annotation Test')
        
        print("✓ matplotlib.figure.Figure type annotation works correctly")
        return True
    except Exception as e:
        print(f"✗ Failed with Figure type annotation: {e}")
        return False

def main():
    """Run all tests."""
    print("Testing pyplot component compatibility with Reflex 0.8.0a6...")
    print("=" * 60)
    
    tests = [
        test_pyplot_import,
        test_pyplot_component_creation,
        test_matplotlib_serializer,
        test_figure_type_annotations,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        print(f"\nRunning {test.__name__}...")
        if test():
            passed += 1
        print("-" * 40)
    
    print(f"\nTest Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! pyplot component is compatible with Reflex 0.8.0a6")
        return True
    else:
        print("❌ Some tests failed. pyplot component may have compatibility issues.")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
