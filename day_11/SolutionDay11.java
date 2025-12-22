package day_11;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class SolutionDay11 {
  public List<String> getLines(String fileName) {
    List<String> lines = new ArrayList<>();
    Class clazz = SolutionDay11.class;
    InputStream inputStream = clazz.getResourceAsStream(fileName);
    try (BufferedReader br = new BufferedReader(new InputStreamReader(inputStream))) {
      String line;
      while ((line = br.readLine()) != null) {
        lines.add(line);
      }
      return lines;
    } catch(IOException e) {
      e.printStackTrace();
    }
    return Collections.emptyList();
  }

  public Node dfs(String name, Map<String, String[]> outputs) {
    if (name.equals("out"))
      return new Node(name);

    Node newNode = new Node(name);
    for (String output : outputs.get(newNode.getName())) {
      newNode.addChild(dfs(output, outputs));
    }
    return newNode;
  }

  public static void main(String[] args) {
    SolutionDay11 sol = new SolutionDay11();
    HashMap<String, String[]> outputs = new HashMap<>();
    for (String line : sol.getLines("../input/11_e.txt")) {
      String[] inputs = line.split(":");
      outputs.put(inputs[0], inputs[1].trim().split(" "));
    }

    Node root = sol.dfs("you", outputs);
  }
}