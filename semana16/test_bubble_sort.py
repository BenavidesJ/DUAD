from bubble_sort import bubble_sort
import pytest

def test_small_list():
    small_list = [-1, 15, 3]
    
    bubble_sort(small_list)
    
    assert small_list == [-1, 3, 15]
    
def test_large_list():
    large_list = [2, 46, 32, 10, 69, 88, 74, 47, 66, 55, 13, 16, 14, 82, 41, 35, 24, 97, 
 60, 84, 79, 61, 67, 44, 49, 81, 94, 98, 33, 19, 42, 23, 77, 78, 17, 43, 
 75, 4, 11, 80, 58, 31, 62, 15, 92, 89, 25, 85, 68, 28, 70, 12, 38, 50, 
 20, 30, 52, 76, 7, 48, 22, 93, 34, 54, 83, 27, 73, 39, 3, 37, 72, 26, 
 95, 63, 65, 86, 40, 6, 99, 8, 36, 5, 59, 96, 9, 18, 53, 56, 91, 57, 29,
 90, 100, 45, 87, 21, 51, 1, 64, 71]
    
    bubble_sort(large_list)
    
    assert large_list == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 
 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 
 93, 94, 95, 96, 97, 98, 99, 100]
    
def test_empty_list():
    empty_list = []
    
    bubble_sort(empty_list)
    
    assert empty_list == []
    
def test_wrong_params():
    with pytest.raises(TypeError):
        bubble_sort('Esto no es una lista')
    with pytest.raises(TypeError):
        bubble_sort(18975)
    with pytest.raises(TypeError):
        bubble_sort({"user": "Jhon"})
    with pytest.raises(TypeError):
        bubble_sort(None)