"""create air"""
import alchemy


print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(
    f"Testing {alchemy.create_air.__name__}: "
    f"{alchemy.create_air()}"
)

print("Now show that not all functions can be reached")
print("This will raise an exception!")
print("Testing the hidden create_earth: ", end="")
print(f"{alchemy.create_earth()}")
try:
    alchemy.create_earth()
except AttributeError as e:
    print(f"AttributeError: {e}. Did you mean: 'create_air'?")