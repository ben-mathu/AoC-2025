package day_11;

import java.util.ArrayList;
import java.util.List;

public class Node {
  private String name;
  private List<Node> children;

  public Node(String name) {
    this.name = name;
    this.children = new ArrayList<>();
  }
  
  public String getName() {
    return name;
  }
  public void setName(String name) {
    this.name = name;
  }
  public List<Node> getChildren() {
    return children;
  }
  
  public void addChild(Node child) {
    this.children.add(child);
  }
}
