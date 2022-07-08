from typing import List


class Utils:
    @staticmethod
    def join_strings(str_list: List[str], enters: bool = False) -> str:
        if enters:
            return "".join(str_list).replace("\n", ",")
        else:
            return "".join(str_list)
