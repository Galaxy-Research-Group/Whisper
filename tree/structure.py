class SonicTree:
    def __init__(self, right=None, left=None, value=None):
        self.right = right
        self.left = left
        self.killswitch = False
        self.value = value


    def is_edge(self):
        return self.right != None and self.left != None
    
    def kill(self):
        tree = self
        while not tree.is_edge():
            tree.killswitch = True
            return tree.right.kill() and tree.left.kill()
        return

    # Simple recursive transmittance --> Will not deactivate
    def transmit(self):
        if not self.killswitch:
            if self.right != None:
                self.right.value = self.value
                self.right.transmit()
            if self.left != None:
                self.left.value = self.value
                self.left.transmit()
    
    # Transmit + Kill on Sight --> Will activate killswitch when condition met
    def transmit_kos(self, condition):
        if (self.right == None and self.left==None):
            return
        if hasattr(self.right, "value") and hasattr(self.left, "value") and condition(self.right.value) or condition(self.left.value) or self.killswitch:
            self.kill() # oof
            return
        else:
            if self.right != None:
                self.right.value = self.value
                self.right.transmit_kos(condition)
            if self.left != None:
                self.left.value = self.value
                self.left.transmit_kos(condition)
        return
            
    
    def __str__(self):
        return "\n\tR:" + str(self.right) + "\tL: " + str(self.left) + "\tS: " + str(self.value)

tree = SonicTree(
                SonicTree(
                    SonicTree(None, None, {"hi":"2"}),
                    SonicTree(None, None, True), False),
                    SonicTree(
                        SonicTree(None, None, {"hi":"5"}),
                        SonicTree(None, None, {"hi":"6"}),
                {"hi":"hello"}),
            {"hi":1})
condition = lambda _: _ == True
tree.transmit_kos(condition)
print(tree)