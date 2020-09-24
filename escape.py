######
# TREENODE CLASS
######
class TreeNode:
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []

    def add_child(self, node):
        self.choices.append(node)

    def traverse(self):
    # assign story_node to self
    # print out story_node's story_piece
    # while story_node has choices:
        # get the user's choice using input()
        # if the choice is invalid
            # tell the user
        # if the choice is valid
            # set choice as the new story_node
        story_node = self
        print(story_node.story_piece)
        while story_node.choices:
            choice = input("Enter 1 or 2 to continue the story: ")
            chosen_index = int(choice) - 1
            if chosen_index in [0, 1]:
                chosen_child = story_node.choices[chosen_index].story_piece
                print(chosen_child)
                story_node = story_node.choices[chosen_index]
            else:
                print("You have not entered a valid response.")
            

######
# VARIABLES FOR TREE
######
user_choice = input("What is your name? ")
print("\nAlright {name}, lets get you started on your jouney!\n".format(name=user_choice))
######
# TESTING AREA
######

print("Once upon a time...")
story_root = TreeNode("'''\nYou are in a forest clearing. There is a path to the left. A bear emerges from the trees and roars!\nDo you:\n1 ) Roar back!\n2 ) Run to the left...\n'''")
choice_a = TreeNode("'''\nThe bear is startled and runs away.\nDo you:\n1 ) Shout 'Sorry bear!'\n2 ) Yell 'Horray!'\n'''")
story_root.add_child(choice_a)
choice_b = TreeNode("'''\nYou come across a clearing full of flowers. The bear follows you and asks 'what gives?'\nDo you:\n1 ) Gasp 'A talking bear!'\n2 ) Explain that the bear scared you.\n'''")
story_root.add_child(choice_b)
choice_a1 = TreeNode("""\nThe bear returns and tells you it's been a rough week. After making peace with a talking bear, he shows you the way out of the forest.\n\nYOU HAVE ESCAPED THE WILDERNESS.\n""")
choice_a.add_child(choice_a1)
choice_a2 = TreeNode("""\nThe bear returns and tells you that bullying is not okay before leaving you alone in the wilderness.\n\nYOU REMAIN LOST.\n""")
choice_a.add_child(choice_a2)
choice_b1 = TreeNode("""\nThe bear is unamused. After smelling the flowers, it turns around and leaves you alone.\n\nYOU REMAIN LOST.\n""")
choice_b.add_child(choice_b1)
choice_b2 = TreeNode("""\nThe bear understands and apologizes for startling you. Your new friend shows you a path leading out of the forest.\n\nYOU HAVE ESCAPED THE WILDERNESS.\n""")
choice_b.add_child(choice_b2)
story_root.traverse()