# Lesson 3 --- Building a Network

**After this lesson, you'll be able to:**

- Find a minimum spanning tree from a network graph.
- Explain why redundancy is important when designing a network.

## Building a network

Alright, let's build a computer network. We want to connect multiple people so they can communicate with each other. Sounds simple enough, right? But there are a few things we need to think about:

- **Connecting everyone** --- every person should be able to communicate with every other person.
- **Saving money** --- cables and infrastructure aren't free.
- **Planning for outages** --- cables break, power fails, squirrels chew through things (this actually happens more than you'd think).

In computer science, we use **graphs** to solve these kinds of problems. And heads up --- these aren't the same as the "graphs" you've seen in statistics class (bar charts, pie charts, &c.). In CS, a graph is a set of **nodes** (points) connected by **edges** (lines). It's a completely different thing that just happens to share a name. Isn't that annoying?

> **Try it yourself!** Sketch the graph in Figure 2.3 on paper and find the minimum (shortest) path to connect every node. Remove redundant paths and add up the total cost.
>
> ![Network graph](../images/network%20graph.png)
> *Figure 2.3. Network graph*

<details>
<summary>Show Solution</summary>

Figure 2.4 shows one solution --- the total cost is **26**. Did you find a lower cost? The optimal solution is called a **minimum spanning tree**. It's the cheapest way to connect all the nodes without any loops.

![Network graph solution: Path C-D-E-I, A-B-D, G-H, E-F-H-J](../images/network%20graph%20solution.png)
*Figure 2.4. Network graph solution*

</details>

We found the shortest-path graph with the cheapest route to connect all of the nodes. But here's the thing --- is this the most efficient way to get from node C to node I? That's actually a different question than "what's the cheapest way to connect everything." Computer scientists are *still* working on better solutions to this type of problem.

> **Try it yourself!** Suppose all of the paths are built (not just the minimum spanning tree). What's the cheapest (shortest) path from node C to node I? What's the cost?

<details>
<summary>Show Solution</summary>

The cheapest path would be C to D to E to I, with a cost of 3 + 5 + 3 = **11**.

</details>

> **Try it yourself!** If node E fails, what would be the new cheapest (shortest) path from C to I?

<details>
<summary>Show Solution</summary>

The cheapest path would be C to D to F to H to I, with a cost of 3 + 6 + 2 + 5 = **16**. Notice how much more expensive it gets when one node goes down --- that's why redundancy matters!

</details>

## Network graph simulator

Want to see an algorithm do this for you? Open this [network graph simulator widget](https://graphonline.ru/en/?graph=PJEevEkiDMxTwWnB) and try it out. Click on the **Algorithms** menu and select "Search of minimum Spanning Tree." Is this the same route you discovered by hand?

Now click on "Find shortest path..." and choose 2 nodes to find the shortest path between them. Pretty satisfying to watch, honestly.

## Redundancy

When we kept *all* the paths instead of trimming down to the minimum spanning tree, we created what's called a **redundant network**. A redundant network has multiple pathways among its physical connections. Even if one pathway goes down, there's still another way to get a message from sender to receiver.

Look at what happens in the animation in Figure 2.5 when a lightning bolt strikes one of the nodes. (Dramatic, but it gets the point across.) There are many reasons a node can fail --- power failure, chip burnout, &c. And it's not just nodes that can go down. The connections between nodes (those green lines) can fail too --- a cable could be cut or disconnected, either accidentally or on purpose.

![Redundant network animation showing alternate path when one path has an outage](../images/redundancy.gif)
*Figure 2.5. Network simulation (Image Source: [BJC Curriculum](https://bjc.edc.org/))*

The takeaway? Redundancy costs more upfront, but it keeps the network alive when things go wrong. And things *always* go wrong eventually.

In the next lesson, we'll learn about **routers** --- the computers that actually move information through the network. Think of them as the postal workers of the internet.
