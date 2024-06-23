def Solution(matches: list[list[int]]) -> list[list[int]]:
  losers = {}  # словник для відстеження кількості програшів кожного гравця

  # Проходимо через кожен матч і оновлюємо кількість програшів
  for match in matches:
      winner, loser = match
      if loser not in losers:
          losers[loser] = 0
      losers[loser] += 1

      # Переконайтеся, що переможці також є у словнику, з нульовою кількістю програшів
      if winner not in losers:
          losers[winner] = 0

  # Збираємо гравців, які не програли жодного разу або програли лише один раз
  zero_losses = [player for player, losses in losers.items() if losses == 0]
  one_loss = [player for player, losses in losers.items() if losses == 1]

  return [sorted(zero_losses), sorted(one_loss)]

matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
print(Solution(matches))
