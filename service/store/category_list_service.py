from model import CategoryListDao


class CategoryListService:
    """ Business Layer

        Attributes:
            category_list_dao : CategoryListDao 클래스

        Author: 김민구

        History:
            2020-12-30(김민구): 초기 생성
            2020-12-31(김민구): 수정 (category_list_dao를 import 해서 사용하는 방법으로 수정)
    """

    def __init__(self):
        self.category_list_dao = CategoryListDao()

    def category_list_logic(self, connection):
        """ 3가지 카테고리 조회

            Args:
                connection : 데이터베이스 연결 객체

            Author: 김민구

            Returns:
                {
                    'menus': first_category_list,
                    'main_categories': second_category_list,
                    'sub_categories': third_category_list
                }

            History:
                2020-12-30(김민구): 초기 생성
        """

        first_category_list = self.category_list_dao.get_first_category_list(connection)
        second_category_list = self.category_list_dao.get_second_category_list(connection)
        third_category_list = self.category_list_dao.get_third_category_list(connection)
        return {
            'menus': first_category_list,
            'main_categories': second_category_list,
            'sub_categories': third_category_list
        }