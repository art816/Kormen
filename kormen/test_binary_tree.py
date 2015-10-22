__author__ = 'art'

import unittest
import random
import copy

import binary_tree


class Test(unittest.TestCase):
    """

    """
    def setUp(self):
        self.tree = None

    def test_create_list(self):
        """

        :return:
        """
        list_object = binary_tree.ListObject(5)
        self.assertTrue(list_object)
        self.assertEqual(list_object.key, 5)
        self.assertEqual(list_object.left, None)
        self.assertEqual(list_object.right, None)
        self.assertEqual(list_object.parent, None)

    def test_create_tree(self):
        """

        :return:
        """
        tree = binary_tree.Tree()
        self.assertTrue(tree)
        self.assertEqual(tree.root, None)

    def test_insert_list(self):
        """

        :return:
        """
        list_object = binary_tree.ListObject(10)
        tree = binary_tree.Tree()
        tree.tree_insert(list_object)
        self.assertEqual(tree.root, list_object)
        self.assertEqual(tree.high, 1)
        list_object_left = binary_tree.ListObject(1)
        tree.tree_insert(list_object_left)
        self.assertEqual(tree.root.left, list_object_left)
        self.assertEqual(tree.high, 2)
        list_object_right = binary_tree.ListObject(19)
        tree.tree_insert(list_object_right)
        self.assertEqual(tree.root.right, list_object_right)
        self.assertEqual(tree.high, 2)
        new_list = binary_tree.ListObject(9)
        tree.tree_insert(new_list)
        self.assertEqual(tree.root.left.right, new_list)
        self.assertEqual(tree.high, 3)
        a = tree.inorder_tree_walk(tree.root)
        print(a)
        print(tree)

    def test_maximum(self):
        """

        :return:
        """
        list_value = self.create_random_tree(100)
        self.assertEqual(self.tree.tree_maximum(self.tree.root).key,
                           max(list_value))

    def test_minimum(self):
        """

        :return:
        """
        list_value = self.create_random_tree(100)
        self.assertEqual(self.tree.tree_minimum(self.tree.root).key,
                           min(list_value))

    def create_random_tree(self, num_element):
        """

        :return:
        """
        self.tree = binary_tree.Tree()
        list_value = []
        for i in range(num_element):
            list_value.append(random.randint(1, 100))
            list_object = binary_tree.ListObject(list_value[-1])
            self.tree.tree_insert(list_object)
        return list_value

    def test_search(self):
        """

        """
        list_value = self.create_random_tree(100)
        list_object = self.tree.tree_search(self.tree.root, list_value[10])
        self.assertEqual(list_object.key, list_value[10])

    def test_successor(self):
        list_value = self.create_random_tree(100)
        curr_value = list_value[10]
        list_object = self.tree.tree_search(self.tree.root, curr_value)
        succes_list = self.tree.tree_successor(list_object)
        sorted_list = sorted(list_value)
        curr_index = sorted_list.index(curr_value)
        self.assertEqual(succes_list.key, sorted_list[curr_index + 1])

    def test_transplant(self):
        list_value = self.create_random_tree(100)
        curr_value = list_value[10]
        list_object = self.tree.tree_search(self.tree.root, curr_value)
        sub_tree1 = self.tree.inorder_tree_walk(list_object.right)
        # проверка, что можем заменить поддерево с корневым узлом list_object
        # поддеревом с корневым узлом list)object.right
        if list_object == list_object.parent.right:
            self.tree.transplant(list_object, list_object.right)
            self.assertEqual(list_object.right, list_object.parent.right)
            sub_tree2 = self.tree.inorder_tree_walk(list_object.parent.right)
        else:
            self.tree.transplant(list_object, list_object.right)
            self.assertEqual(list_object.right, list_object.parent.left)
            sub_tree2 = self.tree.inorder_tree_walk(list_object.parent.left)
        self.assertEqual(sub_tree1, sub_tree2)

    def test_delete(self):
        list_value = self.create_random_tree(100)
        curr_value = list_value[10]
        list_object = self.tree.tree_search(self.tree.root, curr_value)
        self.tree.delete_list(list_object)
        #TODO
        #не знаю как нормально проверь, что правильно удалили элемент,
        # кроме как проверить, что возвращается сортированый список значений.
        res_value = self.tree.inorder_tree_walk(self.tree.root)
        string_res = str(res_value)
        list_with_string = string_res.replace('(', '').\
                                          replace(')', '').\
                                          replace('None', '').\
                                          replace(',', '').\
                                          rsplit('  ')
        list_value = [int(num) for num in list_with_string]
        self.assertEqual(list_value, sorted(list_value))





if __name__ == '__main__':
    unittest.main()