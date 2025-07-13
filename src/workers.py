import torch
import syft as sy

def create_workers():
    hook = sy.TorchHook(torch)
    alice = sy.VirtualMachine(name="alice").get_root_client()
    bob = sy.VirtualMachine(name="bob").get_root_client()
    charlie = sy.VirtualMachine(name="charlie").get_root_client()
    return alice, bob, charlie
