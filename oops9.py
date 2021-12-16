class Dad:
    basketball=8

class Son(Dad):
    dance=1
    basketball=6
    def isdance(self):
        return f"yes i dance {self.dance} no of times"

class Grandson(Son):
    dance=5

    # def isdance(self):
    #     return f"jackson yeah! " \
    #            f"yes i dance very awesomely {self.dance} no of times"

parry=Dad()
carry=Son()
narry=Grandson()

print(narry.isdance())
print(narry.basketball)

# electronic device
# pocket gadget
# phone