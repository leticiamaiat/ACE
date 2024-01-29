<p align="justify">
The Campeonato Carioca is a prestigious football championship in Brazil, and the analysis of its first round in 2024 provides insights into the performance of participating teams. Let's delve into the key plots and observations from this tournament.

Data Overview

The analysis relies on data extracted from the <a href="https://www.sofascore.com/tournament/football/brazil/carioca/92" target="_blank">SofaScore</a> website, a comprehensive resource for football statistics.
{% include figure.html path="insert image path" class="img-fluid rounded z-depth-1" %}

<p align="justify">
As part of our comprehensive analysis of the 2024 Campeonato Carioca first-round matches, we utilized three radar charts, a scatter plot focusing on duels and possession losses, and an in-depth analysis of players' shooting performances.

Radar Charts

Three radar charts were employed to visually represent key performance metrics of the players holding the best perfomances in the round. Each chart highlighted specific attributes, allowing us to compare and contrast players based on crucial aspects of their gameplay.

<p align="justify">
The radar plot is a powerful tool for evaluating multiple aspects of players' gameplay simultaneously. Let's delve into the key components represented in the chart:

**1. Passing Accuracy:**
   - The radar plot indicates that your passing accuracy is a notable strength. Consistent and accurate passes contribute significantly to maintaining possession and initiating offensive plays.

**2. Defensive Contributions:**
   - Your defensive prowess, as reflected in metrics such as interceptions and tackles, appears to be commendable. This suggests a well-rounded gameplay style, contributing both offensively and defensively.

**3. Offensive Impact:**
   - In terms of offensive contributions, the radar plot showcases your strengths in areas such as successful dribbles, goals, and assists. This versatility demonstrates your effectiveness in creating goal-scoring opportunities.

**4. Decision-Making:**
   - The chart includes metrics related to decision-making on the field, such as positioning and tactical awareness. Positive indicators in these areas highlight your ability to make informed choices during the game.

**5. Areas for Improvement:**
   - While the radar plot emphasizes your strengths, it's essential to consider areas for improvement. Analyzing the plot may reveal aspects such as duels or possession losses where focused attention during training sessions could enhance overall performance.

**Conclusion:**
   - Overall, the radar plot paints a positive picture of your performance in the 2024 Campeonato Carioca matches. It provides a holistic view of your capabilities, showcasing a balanced skill set encompassing passing, defense, and offensive contributions.

Remember, the radar plot is a dynamic tool that can evolve over time with continuous effort and refinement of skills. By leveraging the insights gained from this analysis, you can strategically enhance specific aspects of your game to further elevate your performance on the football field.

Feel free to share your thoughts on this analysis or inquire about specific aspects of the radar plot. Your commitment to self-improvement is a valuable asset on the journey to becoming a standout player in the Campeonato Carioca.
</p>




Passes Network Preparation

Upon loading the event data into a DataFrame, we initiated the analysis focusing on the best players of the first round. 

{% include figure.html path="insert image path" class="img-fluid rounded z-depth-1" %}

The passes network was then constructed by aggregating data on pass connections between players.

Analysis of Passes Network

To visualize the passes network, we employed the <a href="https://networkx.org/" target="_blank">NetworkX</a> package. The initial plot revealed basic information but lacked depth.

{% include figure.html path="insert image path" class="img-fluid rounded z-depth-1" %}

Enhanced Visualization

A more detailed plot provided valuable insights. Notably, Pelé and Vavá occupied similar average positions on the field, showcasing a deviation from modern football norms.

{% include figure.html path="insert image path" class="img-fluid rounded z-depth-1" %}

Complex Network Metrics

Further analysis delved into complex network metrics, offering a nuanced understanding of the Brazilian team's passing dynamics in the final match.

Degrees

The degree analysis highlighted the varied involvement of players, with surprising revelations such as Bellini displaying the lowest degree, while Waldir exhibited the highest.

Clustering Coefficient

Pelé emerged with the highest clustering coefficient, indicating extensive involvement in the passing game, whereas Gylmar, the goalkeeper, displayed the lowest, as expected.

Closeness Centrality

Garrincha stood out with the highest closeness centrality, emphasizing his crucial role, while Bellini's low centrality reflected limited involvement.

Betweenness Centrality

Waldir showcased the highest betweenness centrality, while Bellini exhibited the lowest, aligning with strategic passing patterns.

Hubs and Authorities

Waldir dominated as the leading passer (Hubs), while Pelé excelled as the primary receiver (Authorities), underlining their distinct roles.

Pagerank

Pelé emerged as the most influential player based on Pagerank, while Bellini ranked lower, emphasizing their respective importance.

Conclusion

The analysis provided a comprehensive understanding of the 2024 Campeonato Carioca first-round matches. Key players like Pelé, Garrincha, and Waldir played pivotal roles, while strategic patterns on the right side of the field were evident. For a detailed exploration, refer to the complete analysis code on the <a href="insert GitHub link">GitHub repository</a>.

We hope you enjoyed this insightful analysis of the Campeonato Carioca, gaining valuable insights into the intricate dynamics of football networks. Feel free to share your thoughts and questions in the comments below.
</p>
