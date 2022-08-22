class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        amountOfMoneyValues = map(lambda accountByPerson: sum(accountByPerson), accounts)
        return max(amountOfMoneyValues)