from cq09.point import Point

first_point = Point(1.5, 2.2)
print(f"Original Point: {first_point.x}, {first_point.y}")

second_point = first_point.scale(2)
print(f"New Point (scaled): ({second_point.x}, {second_point.y})")
print(
    f"Original Point after scale: ({first_point.x}, {first_point.y})"
)  # (should be unchanged)

first_point.scale_by(2)
print(
    f"Original Point after scale_by: ({first_point.x}, {first_point.y})"
)  # (should be mutated)
