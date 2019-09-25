import uuid

class SonicTree:
    def __init__(self, right=None, left=None, value=None):
        "TEMP"
        self.right = right
        self.left = left
        ""
        """
        FUTURE:
        self.nodes = nodes
        """
        self.killswitch = False
        self.value = value
        self.id= str(uuid.uuid4())
        self.keypairs = {}


    def is_edge(self):
        return self.right == None and self.left == None
    
    def kill(self):
        tree = self
        while not tree.is_edge():
            tree.killswitch = True
            return tree.right.kill() and tree.left.kill()
        return
    
    @staticmethod
    def gen_key():
        return str(uuid.uuid4()) # temp

    def gen_keypair(self):
        tree = self
        while not tree.is_edge():
            if tree.right != None:
                key = SonicTree.gen_key()
                tree.keypairs[tree.right.id] = key
                tree.right.keypairs[tree.id] = key
            if tree.left  != None:
                key = SonicTree.gen_key()
                tree.keypairs[tree.left.id] = key
                tree.left.keypairs[tree.id] = key
            return tree.right.gen_keypair() and tree.left.gen_keypair()
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
        return "\n\tR:" + str(self.right) + "\tL: " + str(self.left) + "\tS: " + str(self.value) + "\tK: " + str(self.keypairs)

tree = SonicTree(
                SonicTree(
                    SonicTree(None, None, {"hi":"2"}),
                    SonicTree(None, None, False), False),
                    SonicTree(
                        SonicTree(None, None, {"hi":"5"}),
                        SonicTree(None, None, True),
                {"hi":"hello"}),
            {"hi":1})
tree.gen_keypair()
print(tree)