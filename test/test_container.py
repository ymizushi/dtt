from dtt.dock.container import Containers

def test_containers():
    test_containers = Containers(
        [1, 2, 3, 4, 5]
    )
    test_containers.set_index(3)
    assert  test_containers.index == 3 
    assert  test_containers.current_container == 4 
    assert  test_containers.list ==  [1, 2, 3, 4, 5]

    test_containers.add_index()
    assert  test_containers.index == 4
    test_containers.sub_index()
    assert  test_containers.index == 3
