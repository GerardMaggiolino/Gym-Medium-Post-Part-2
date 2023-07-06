import gym
import torch
from agent import TRPOAgent
import simple_driving
import time


def main():
    nn = torch.nn.Sequential(torch.nn.Linear(8, 64), torch.nn.Tanh(),
                             torch.nn.Linear(64, 2))
    
    #TODO: Add noise parameters into init (Check init for TRPO agents for which parameter is which)
    agent = TRPOAgent(policy=nn, input_noise=True, output_noise=True, weight_one_noise=True, weight_two_noise=True)

    #agent.load_model("models/Model Reward=24.967.pth")
    agent.train("SimpleDriving-v0", seed=0, batch_size=5000, iterations=100,
                max_episode_length=250, verbose=True)
    #agent.save_model("models/")
    agent.save_best_agent("models/")

    '''
    env = gym.make('SimpleDriving-v0')
    ob = env.reset()
    env.render()
    
    while True:
        action = agent(ob)
        ob, _, done, _ = env.step(action)
        env.render()
        if done:
            ob = env.reset()
            time.sleep(1/30)
    '''
    

if __name__ == '__main__':
    main()
