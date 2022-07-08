# SPDX-FileCopyrightText: AISEC Pentesting Team
#
# SPDX-License-Identifier: Apache-2.0

from argparse import Namespace

from gallia.command import Scanner, load_transport
from gallia.services.xcp import XCPService
from gallia.utils import catch_and_exception


class SimpleTestXCP(Scanner):
    """Test XCP Slave"""

    async def main(self, args: Namespace) -> None:
        transport = load_transport(args.target)
        await transport.connect(None)
        service = XCPService(transport)

        await catch_and_exception(self.logger, service.connect)
        await catch_and_exception(self.logger, service.get_status)
        await catch_and_exception(self.logger, service.get_comm_mode_info)
        await catch_and_exception(self.logger, service.disconnect)
