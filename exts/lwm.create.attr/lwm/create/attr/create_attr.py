import omni.usd
from pxr import Usd, Sdf, UsdGeom
import random

stage = omni.usd.get_context().get_stage()
cube_mesh = UsdGeom.Mesh.Define(stage, "/World/Cube")
cube_path = "/World/Cube"
cube = stage.GetPrimAtPath(cube_path)
color_attr = cube.CreateAttribute("new_color", Sdf.ValueTypeNames.Color3fArray)

cube_duplicates = 4

for i in range(cube_duplicates):
    mesh_name = f"/World/Cube_{i}"
    cube_mesh_duplicates = UsdGeom.Mesh.Define(stage, mesh_name)
    cube_mesh_path = stage.GetPrimAtPath(mesh_name)
    color_attr = cube_mesh_path.CreateAttribute("new_color", Sdf.ValueTypeNames.Color3fArray)

    values = [(random.uniform(0,1),random.uniform(0,1), random.uniform(0,1))]
    color_attr.Set(values)


