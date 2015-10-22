__author__ = 'art'

import unittest
import random

import red_black_tree


class Test(unittest.TestCase):
    """

    """
    @classmethod
    def setUpClass(cls):
        cls.num_element = []
        cls.num_element.append(200)
        cls.tree = red_black_tree.Tree()
        cls.list_value = cls.create_random_tree(cls)

    # def setUp(self):
    #     self.num_element[0] = 200
    #     self.tree = red_black_tree.Tree()
    #     self.list_value = self.create_random_tree()

    def create_random_tree(self):
        """дфшра дфруша фжцуазэуцаоуцаушрафушар666дшо6фу6дшфудша2уар2цуа5а◘уа8ибфцуоиафцуиа

        :return:
        """
        list_value = []
        for i in range(self.num_element[0]):
            list_value.append(random.randint(1, 100))
            list_object = red_black_tree.ListObject(list_value[-1])
            self.tree.tree_insert(list_object)
        assert(self.tree.root.size == self.num_element[0])
        return list_value

    def test_tree(self):
        """

        :return:
        """
        self.assertEqual(self.tree.root.color, 'black')
        self.assertEqual(self.tree.nil.color, 'black')

    def test_red_black(self):
        """
        :param list_object must be root
        :return:
        """
        if self.tree.root is not self.tree.nil:
            self.red_list_have_black_child(self.tree.root)

    def red_list_have_black_child(self, list_object):
        """
        :param list_object:
        :return:
        """
        if list_object is not self.tree.nil:
            if list_object.color == 'red':
                self.assertEqual(list_object.left.color, 'black')
                self.assertEqual(list_object.right.color, 'black')
            self.red_list_have_black_child(list_object.left)
            self.red_list_have_black_child(list_object.right)

    def test_len_simple_road(self):
        """
        :return:
        """
        # TODO patern
        rez_string = str(self.len_sub_tree(self.tree.root))
        centr = rez_string.find('root')
        count = -1
        max_count = 0
        for i in range(centr):
            if rez_string[i] == '(':
                count += 1
            elif rez_string[i] == ')':
                count -= 1
            if count > max_count:
                max_count = count
        count = 1
        max_count = 0
        open_tree = False
        depth_tree = 0
        rb_depth_tree = 0
        for i in range(centr, len(rez_string)):
            if rez_string[i] == '(':
                count += 1
                if open_tree:
                    depth_tree += 1
            elif rez_string[i] == ')':
                count -= 1
                if open_tree:
                    depth_tree -= 1
                    if depth_tree == 0:
                        open_tree = False
            if rez_string[i:i + 1] == '(1' and open_tree is False:
                open_tree = True
            elif rez_string[i:i + 1] == '(1' and open_tree is True:
                rb_depth_tree += 1
            if count > max_count:
                max_count = count
        res_value = self.tree.inorder_tree_walk(self.tree.root)

    def len_sub_tree(self, list_object):
        """

        :param list_object:
        :return:
        """
        if list_object is not self.tree.nil:
            return (self.len_sub_tree(list_object.left),
                    (
                        'root' if list_object == self.tree.root else 1 if list_object.color == 'black' else 0,
                        list_object.key),
                    self.len_sub_tree(list_object.right))

    # @unittest.skip('dont work')
    def test_transplant(self):
        # self.list_value = self.create_random_tree(1)
        curr_value = self.list_value[random.randint(
                        0, len(self.list_value) - 1)]
        list_object = self.tree.tree_search(self.tree.root, curr_value)
        sub_tree1 = self.tree.inorder_tree_walk(list_object.right)
        # проверка, что можем заменить поддерево с корневым узлом list_object
        # поддеревом с корневым узлом list)object.right
        if list_object == list_object.parent.right:
            diff_size = self.tree.transplant(list_object, list_object.right)
            self.assertEqual(list_object.right, list_object.parent.right)
            sub_tree2 = self.tree.inorder_tree_walk(list_object.parent.right)
        else:
            diff_size = self.tree.transplant(list_object, list_object.right)
            self.assertEqual(list_object.right, list_object.parent.left)
            sub_tree2 = self.tree.inorder_tree_walk(list_object.parent.left)
        self.assertEqual(sub_tree1, sub_tree2)

        # self.tree.return_true_size(list_object.right, diff_size)
        self.assertEqual(self.tree.root.size, self.num_element[0] + diff_size,
                         diff_size)
        self.assertEqual(self.tree.os_rank(self.tree.root),
                         self.tree.root.left.size + 1)
        self.true_size(self.tree.root)

    # @unittest.skip('not work')
    def test_delete(self):
        # self.list_value = self.create_random_tree(100)
        curr_value = self.list_value[random.randint(
                        0, len(self.list_value) - 1)]
        # list_object = self.tree.tree_search(self.tree.root, curr_value)
        list_object = self.tree.tree_minimum(self.tree.root).parent
        self.tree.delete_list(list_object)
        # TODO
        # не знаю как нормально проверить, что правильно удалили элемент,
        # кроме как проверить, что возвращается сортированый список значений.
        res_value = self.tree.inorder_tree_walk(self.tree.root)
        string_res = str(res_value)
        list_with_string = string_res.replace('(', ''). \
            replace(')', ''). \
            replace('None', ''). \
            replace(',', ''). \
            rsplit('  ')
        self.list_value = [int(num) for num in list_with_string]
        self.assertEqual(self.list_value, sorted(self.list_value))
        # self.assertTrue(False)
        self.assertEqual(self.tree.root.size, self.num_element[0] - 1)
        self.assertEqual(self.tree.os_rank(self.tree.root),
                         self.tree.root.left.size + 1)
        self.true_size(self.tree.root)
        self.num_element[0] -= 1
        pass

    def test_select_rank(self):
        """

        :return:
        """
        rank = self.tree.os_rank(self.tree.root) - 1
        list_object = self.tree.os_select(self.tree.root, rank)
        true_result = self.tree.root.left
        while true_result.right is not self.tree.nil:
            true_result = true_result.right
        self.assertEqual(list_object, true_result, (list_object.__dict__,
                                                    true_result.__dict__))
        seach_rank = self.tree.os_rank(list_object)
        self.assertEqual(rank, seach_rank)

    def test_root_rank(self):
        """

        :return:
        """
        seach_rank = self.tree.os_rank(self.tree.root)
        self.assertEqual(seach_rank, self.tree.root.left.size + 1)
        self.assertEqual(self.tree.root.left.size +
                            self.tree.root.right.size + 1,
                         self.tree.root.size)
        self.assertEqual(self.tree.root.left.size +
                            self.tree.root.right.size + 1,
                         self.num_element[0])

    def true_size(self, list_object):
        """

        :param list_object: must be root
        :return:
        """
        if list_object is not self.tree.nil:
            self.assertEqual(list_object.size, list_object.left.size +
                                               list_object.right.size + 1)
            self.true_size(list_object.left)
            self.true_size(list_object.right)